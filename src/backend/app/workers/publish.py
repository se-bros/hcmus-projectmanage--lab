import html
import logging
import subprocess
import tempfile
import uuid
import zipfile
from collections.abc import Callable
from pathlib import Path, PurePosixPath
from typing import Protocol
from xml.etree import ElementTree

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.storage import minio_client
from app.db.session import SessionLocal
from app.models.page import Page
from app.models.publish_job import PublishJob
from app.services.publish_service import validate_publishable

logger = logging.getLogger(__name__)


class StorageClient(Protocol):
    def put_object(self, **kwargs: object) -> object: ...


def _normalize_text(value: str) -> str:
    return " ".join(value.split())


def _write_source_html(path: Path, title: str, author: str, pages: list[Page]) -> None:
    sections = []
    for page in pages:
        page_text = html.escape(page.text_content).replace("\n", "<br>\n")
        sections.append(
            f'<section data-page-number="{page.page_number}">'
            f"<h1>Page {page.page_number}</h1><div>{page_text}</div></section>"
        )
    source = (
        '<!doctype html><html><head><meta charset="utf-8">'
        f"<title>{html.escape(title)}</title>"
        f'<meta name="author" content="{html.escape(author)}">'
        "</head><body>" + "\n".join(sections) + "</body></html>"
    )
    path.write_text(source, encoding="utf-8")


def _create_epub(source_html: Path, output_epub: Path, title: str, author: str) -> None:
    subprocess.run(
        [
            "pandoc",
            str(source_html),
            "--from=html",
            "--to=epub3",
            f"--metadata=title:{title}",
            f"--metadata=author:{author}",
            f"--output={output_epub}",
        ],
        check=True,
        capture_output=True,
        text=True,
        timeout=settings.pandoc_timeout_seconds,
    )


def _epub_spine_text(archive: zipfile.ZipFile, opf_path: str, root: ElementTree.Element) -> str:
    namespace = {"opf": "http://www.idpf.org/2007/opf"}
    manifest = {
        item.attrib["id"]: item.attrib["href"]
        for item in root.findall(".//opf:manifest/opf:item", namespace)
        if "id" in item.attrib and "href" in item.attrib
    }
    opf_directory = PurePosixPath(opf_path).parent
    chunks: list[str] = []
    for itemref in root.findall(".//opf:spine/opf:itemref", namespace):
        href = manifest.get(itemref.attrib.get("idref", ""))
        if href is None:
            continue
        entry = str(opf_directory / href)
        xhtml_root = ElementTree.fromstring(archive.read(entry))
        chunks.append(" ".join(xhtml_root.itertext()))
    return _normalize_text(" ".join(chunks))


def validate_epub(path: Path, title: str, author: str, pages: list[Page]) -> None:
    with zipfile.ZipFile(path) as archive:
        names = archive.namelist()
        if "mimetype" not in names or archive.read("mimetype") != b"application/epub+zip":
            raise RuntimeError("Generated file is not a valid EPUB archive.")
        if "META-INF/container.xml" not in names:
            raise RuntimeError("Generated EPUB has no container.xml.")

        container = ElementTree.fromstring(archive.read("META-INF/container.xml"))
        rootfile = container.find(".//{*}rootfile")
        if rootfile is None or "full-path" not in rootfile.attrib:
            raise RuntimeError("Generated EPUB has no package document.")
        opf_path = rootfile.attrib["full-path"]
        package = ElementTree.fromstring(archive.read(opf_path))
        epub_title = package.findtext(".//{http://purl.org/dc/elements/1.1/}title") or ""
        epub_author = package.findtext(".//{http://purl.org/dc/elements/1.1/}creator") or ""
        if _normalize_text(epub_title) != _normalize_text(title):
            raise RuntimeError("Generated EPUB title does not match document metadata.")
        if _normalize_text(epub_author) != _normalize_text(author):
            raise RuntimeError("Generated EPUB author does not match document metadata.")

        spine_text = _epub_spine_text(archive, opf_path, package)
        cursor = 0
        for page in pages:
            expected = _normalize_text(page.text_content)
            position = spine_text.find(expected, cursor)
            if position < 0:
                raise RuntimeError(
                    f"Generated EPUB does not contain page {page.page_number} in order."
                )
            cursor = position + len(expected)


def _mark_failed(
    job_id: uuid.UUID,
    message: str,
    session_factory: Callable[[], Session],
) -> None:
    with session_factory() as db:
        job = db.get(PublishJob, job_id)
        if job is None:
            return
        job.status = "failed"
        job.error_message = message[:4000]
        job.document.status = "publish_failed"
        db.commit()


def run_publish_job(
    job_id: uuid.UUID,
    session_factory: Callable[[], Session] = SessionLocal,
    storage_client: StorageClient | None = None,
) -> None:
    client = storage_client or minio_client
    try:
        with session_factory() as db:
            job = db.get(PublishJob, job_id)
            if job is None or job.status != "pending":
                return
            job.status = "publishing"
            job.error_message = None
            job.document.status = "publishing"
            db.commit()

            document = job.document
            pages = validate_publishable(db, document)
            document_id = document.id
            title = (document.title or "").strip()
            author = (document.author or "").strip()

            with tempfile.TemporaryDirectory(prefix=f"publish-{job_id}-") as temporary_directory:
                workdir = Path(temporary_directory)
                source_html = workdir / "document.html"
                output_epub = workdir / "document.epub"
                _write_source_html(source_html, title, author, pages)
                _create_epub(source_html, output_epub, title, author)
                validate_epub(output_epub, title, author, pages)

                epub_object_key = f"documents/{document_id}/epub/{job_id}.epub"
                with output_epub.open("rb") as epub:
                    client.put_object(
                        bucket_name=settings.minio_bucket,
                        object_name=epub_object_key,
                        data=epub,
                        length=output_epub.stat().st_size,
                        content_type="application/epub+zip",
                    )

            with session_factory() as db:
                job = db.get(PublishJob, job_id)
                if job is None or job.status != "publishing":
                    return
                job.status = "completed"
                job.error_message = None
                job.document.epub_object_key = epub_object_key
                job.document.status = "published"
                db.commit()
    except Exception as exc:
        logger.exception("Publish job %s failed", job_id)
        try:
            _mark_failed(job_id, str(exc) or exc.__class__.__name__, session_factory)
        except Exception:
            logger.exception("Could not persist failure for publish job %s", job_id)


def recover_interrupted_publish_jobs(
    session_factory: Callable[[], Session] = SessionLocal,
) -> int:
    with session_factory() as db:
        jobs = list(
            db.scalars(select(PublishJob).where(PublishJob.status.in_(("pending", "publishing"))))
        )
        for job in jobs:
            job.status = "failed"
            job.error_message = "Publish interrupted by API restart; start publishing again."
            job.document.status = "publish_failed"
        db.commit()
        return len(jobs)
