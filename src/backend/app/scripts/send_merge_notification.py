"""Notify all repo contributors by email after a merge to main, via Brevo's HTTP API."""

from __future__ import annotations

import os
import sys
from pathlib import Path

import httpx

BREVO_API_URL = "https://api.brevo.com/v3/smtp/email"
RECIPIENTS_FILE = Path(__file__).resolve().parents[4] / ".github" / "ci-notify-recipients.txt"


def parse_recipients(text: str) -> list[str]:
    recipients = []
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        recipients.append(line)
    return recipients


def build_payload(
    *,
    sender_email: str,
    recipients: list[str],
    repo: str,
    branch: str,
    commit_sha: str,
    commit_message: str,
    commit_author: str,
    commit_url: str,
    run_url: str,
) -> dict:
    short_sha = commit_sha[:7]
    first_line = commit_message.splitlines()[0] if commit_message else short_sha
    subject = f"[{repo}] Merged to {branch}: {first_line}"
    html_content = (
        f"<p><strong>{repo}</strong> vừa merge vào <strong>{branch}</strong>.</p>"
        "<ul>"
        f'<li>Commit: <a href="{commit_url}">{short_sha}</a></li>'
        f"<li>Tác giả: {commit_author}</li>"
        f"<li>Message: {commit_message}</li>"
        f'<li>Workflow run: <a href="{run_url}">{run_url}</a></li>'
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
    api_key = os.environ["BREVO_API_KEY"]
    sender_email = os.environ["BREVO_SENDER_EMAIL"]
    repo = os.environ["GITHUB_REPOSITORY"]
    branch = os.environ.get("GITHUB_REF_NAME", "main")
    commit_sha = os.environ["GITHUB_SHA"]
    commit_message = os.environ.get("COMMIT_MESSAGE", "")
    commit_author = os.environ.get("COMMIT_AUTHOR", "")
    server_url = os.environ.get("GITHUB_SERVER_URL", "https://github.com")
    run_id = os.environ.get("GITHUB_RUN_ID", "")

    recipients = parse_recipients(RECIPIENTS_FILE.read_text())
    if not recipients:
        print("No recipients configured, skipping email.")
        return 0

    payload = build_payload(
        sender_email=sender_email,
        recipients=recipients,
        repo=repo,
        branch=branch,
        commit_sha=commit_sha,
        commit_message=commit_message,
        commit_author=commit_author,
        commit_url=f"{server_url}/{repo}/commit/{commit_sha}",
        run_url=f"{server_url}/{repo}/actions/runs/{run_id}",
    )
    send_email(api_key, payload)
    print(f"Sent merge notification to {len(recipients)} recipient(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
