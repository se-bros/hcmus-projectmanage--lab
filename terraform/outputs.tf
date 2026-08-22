# ==============================================================================
# Terraform Outputs - HCMUS-LDMS Infrastructure Endpoints
# ==============================================================================

output "live_deployment_url" {
  description = "Public live production application URL"
  value       = var.live_app_url
}

output "local_web_url" {
  description = "Local Nginx Web Frontend URL"
  value       = "http://localhost:${var.web_port}"
}

output "local_api_url" {
  description = "Local FastAPI Backend URL"
  value       = "http://localhost:${var.api_port}"
}

output "local_api_docs_url" {
  description = "Local FastAPI OpenAPI / Swagger Docs URL"
  value       = "http://localhost:${var.api_port}/docs"
}

output "minio_console_url" {
  description = "MinIO Object Storage Web Console URL"
  value       = "http://localhost:${var.minio_console_port}"
}

output "mailhog_ui_url" {
  description = "MailHog SMTP Web UI URL"
  value       = "http://localhost:${var.mailhog_ui_port}"
}

output "grafana_dashboard_url" {
  description = "Grafana Monitoring Dashboard URL"
  value       = "http://localhost:${var.grafana_port}"
}

output "prometheus_metrics_url" {
  description = "Prometheus Metrics Server URL"
  value       = "http://localhost:${var.prometheus_port}"
}

output "postgres_connection_string" {
  description = "PostgreSQL Local Database Connection String"
  value       = "postgresql://${var.postgres_user}:${var.postgres_password}@localhost:${var.postgres_port}/${var.postgres_db}"
  sensitive   = true
}
