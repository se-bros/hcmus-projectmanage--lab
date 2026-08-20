from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_returns_ok():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_metrics_returns_prometheus_data():
    response = client.get("/metrics")
    assert response.status_code == 200
    assert (
        "http_requests_total" in response.text
        or "http_request_duration_seconds" in response.text
        or "process_cpu_seconds_total" in response.text
    )
