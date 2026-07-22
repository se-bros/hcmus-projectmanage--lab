import httpx
import pytest

from app.scripts.send_merge_notification import (
    build_payload,
    compute_overall_status,
    parse_recipients,
    send_email,
)


def test_parse_recipients_skips_blank_and_comment_lines():
    text = """
    # comment
    a@example.com

    b@example.com
    """.replace("    ", "")
    assert parse_recipients(text) == ["a@example.com", "b@example.com"]


def test_parse_recipients_empty_text():
    assert parse_recipients("") == []


def test_compute_overall_status_all_success():
    assert compute_overall_status({"backend": "success", "frontend": "success"}) == "success"


def test_compute_overall_status_any_failure():
    assert compute_overall_status({"backend": "success", "frontend": "failure"}) == "failure"


def test_compute_overall_status_empty():
    assert compute_overall_status({}) == "unknown"


def test_build_payload_uses_first_line_of_message_as_subject():
    payload = build_payload(
        sender_email="ci@example.com",
        recipients=["a@example.com", "b@example.com"],
        repo="org/repo",
        branch="main",
        commit_sha="abcdef1234567",
        commit_message="fix: bug\n\nlonger body",
        commit_author="alice",
        commit_url="https://github.com/org/repo/commit/abcdef1234567",
        run_url="https://github.com/org/repo/actions/runs/1",
        job_statuses={"backend": "success", "frontend": "success"},
    )
    assert payload["sender"] == {"email": "ci@example.com"}
    assert payload["to"] == [{"email": "a@example.com"}, {"email": "b@example.com"}]
    assert payload["subject"] == "[org/repo] ✅ Merged to main: fix: bug"
    assert "abcdef1" in payload["htmlContent"]
    assert "backend: ✅ success" in payload["htmlContent"]
    assert "frontend: ✅ success" in payload["htmlContent"]
    assert "Status: ✅ success" in payload["htmlContent"]


def test_build_payload_reflects_job_failure_in_subject_and_status():
    payload = build_payload(
        sender_email="ci@example.com",
        recipients=["a@example.com"],
        repo="org/repo",
        branch="main",
        commit_sha="abcdef1234567",
        commit_message="fix: bug",
        commit_author="alice",
        commit_url="https://github.com/org/repo/commit/abcdef1234567",
        run_url="https://github.com/org/repo/actions/runs/1",
        job_statuses={"backend": "failure", "frontend": "success"},
    )
    assert payload["subject"].startswith("[org/repo] ❌ Merged to main:")
    assert "backend: ❌ failure" in payload["htmlContent"]
    assert "Status: ❌ failure" in payload["htmlContent"]


def test_send_email_raises_on_http_error(monkeypatch):
    def fake_post(url, headers, json, timeout):
        return httpx.Response(400, request=httpx.Request("POST", url))

    monkeypatch.setattr(httpx, "post", fake_post)

    with pytest.raises(httpx.HTTPStatusError):
        send_email("fake-key", {"sender": {"email": "x@example.com"}})
