"""Notify all repo contributors by email after CD deployment, via Brevo's HTTP API."""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

import httpx

BREVO_API_URL = "https://api.brevo.com/v3/smtp/email"
ROOT_DIR = Path(__file__).resolve().parents[4]
CD_RECIPIENTS_FILE = ROOT_DIR / ".github" / "cd-notify-recipients.txt"
CI_RECIPIENTS_FILE = ROOT_DIR / ".github" / "ci-notify-recipients.txt"

STATUS_EMOJI = {"success": "✅", "failure": "❌", "cancelled": "⚠️", "skipped": "⏭️"}


def parse_recipients(file_path: Path) -> list[str]:
    if not file_path.exists():
        return []
    recipients = []
    for line in file_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        recipients.append(line)
    return recipients


def get_recipients() -> list[str]:
    recipients = parse_recipients(CD_RECIPIENTS_FILE)
    if not recipients:
        recipients = parse_recipients(CI_RECIPIENTS_FILE)
    return recipients


def compute_overall_status(job_statuses: dict[str, str]) -> str:
    if not job_statuses:
        return "unknown"
    if all(status == "success" for status in job_statuses.values()):
        return "success"
    return "failure"


def build_payload(
    *,
    sender_email: str,
    recipients: list[str],
    repo: str,
    branch_or_tag: str,
    deploy_env: str,
    deploy_url: str,
    commit_sha: str,
    commit_message: str,
    commit_author: str,
    commit_url: str,
    run_url: str,
    job_statuses: dict[str, str],
) -> dict:
    short_sha = commit_sha[:7] if commit_sha else "unknown"
    first_line = commit_message.splitlines()[0] if commit_message else short_sha
    overall_status = compute_overall_status(job_statuses)
    status_icon = STATUS_EMOJI.get(overall_status, "🚀")

    subject = f"[{repo}] {status_icon} CD ({deploy_env}) - {branch_or_tag}: {first_line}"

    job_rows = "".join(
        f"<li>{job}: {STATUS_EMOJI.get(status, '')} {status}</li>"
        for job, status in job_statuses.items()
    )

    html_content = (
        f"<p><strong>{repo}</strong> vừa triển khai lên môi trường "
        f"<strong>{deploy_env.upper()}</strong>.</p>"
        f'<p>🌐 <strong>Live URL:</strong> <a href="{deploy_url}">{deploy_url}</a></p>'
        "<ul>"
        f"<li>Branch / Tag: {branch_or_tag}</li>"
        f"<li>Environment: {deploy_env}</li>"
        f'<li>Commit: <a href="{commit_url}">{short_sha}</a></li>'
        f"<li>Author: {commit_author}</li>"
        f"<li>Message: {commit_message}</li>"
        f'<li>Workflow run: <a href="{run_url}">{run_url}</a></li>'
        f"<li>Job run:<ul>{job_rows}</ul></li>"
        f"<li>Status: {STATUS_EMOJI.get(overall_status, '')} {overall_status}</li>"
        "</ul>"
    )

    return {
        "sender": {"email": sender_email},
        "to": [{"email": email} for email in recipients],
        "subject": subject,
        "htmlContent": html_content,
    }


def send_email(api_key: str, payload: dict) -> None:
    response = httpx.post(
        BREVO_API_URL,
        headers={"api-key": api_key, "content-type": "application/json"},
        json=payload,
        timeout=30,
    )
    response.raise_for_status()


def main() -> int:
    api_key = os.environ.get("BREVO_API_KEY")
    sender_email = os.environ.get("BREVO_SENDER_EMAIL")

    if not api_key or not sender_email:
        print("Missing BREVO_API_KEY or BREVO_SENDER_EMAIL, skipping email.")
        return 0

    repo = os.environ.get("GITHUB_REPOSITORY", "se-bros/hcmus-projectmanage--lab")
    branch_or_tag = os.environ.get("GITHUB_REF_NAME", "main")
    deploy_env = os.environ.get("DEPLOY_ENV", "production")
    deploy_url = os.environ.get("DEPLOY_URL", "https://hcmus-projectmanage-lab.vercel.app")
    commit_sha = os.environ.get("GITHUB_SHA", "")
    commit_message = os.environ.get("COMMIT_MESSAGE", "")
    commit_author = os.environ.get("COMMIT_AUTHOR", "")
    server_url = os.environ.get("GITHUB_SERVER_URL", "https://github.com")
    run_id = os.environ.get("GITHUB_RUN_ID", "")
    job_statuses = json.loads(os.environ.get("JOB_STATUSES", "{}"))

    recipients = get_recipients()
    if not recipients:
        print("No recipients configured, skipping email.")
        return 0

    commit_url = (
        f"{server_url}/{repo}/commit/{commit_sha}" if commit_sha else f"{server_url}/{repo}"
    )
    run_url = (
        f"{server_url}/{repo}/actions/runs/{run_id}" if run_id else f"{server_url}/{repo}/actions"
    )

    payload = build_payload(
        sender_email=sender_email,
        recipients=recipients,
        repo=repo,
        branch_or_tag=branch_or_tag,
        deploy_env=deploy_env,
        deploy_url=deploy_url,
        commit_sha=commit_sha,
        commit_message=commit_message,
        commit_author=commit_author,
        commit_url=commit_url,
        run_url=run_url,
        job_statuses=job_statuses,
    )

    try:
        send_email(api_key, payload)
        print(f"Successfully sent CD notification to {len(recipients)} recipient(s).")
    except Exception as exc:
        print(f"Failed to send CD email: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
