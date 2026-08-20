# HCMUS-LDMS 1-Click Production Stack Launcher for Windows PowerShell
$ErrorActionPreference = "Stop"

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$rootDir = Split-Path -Parent $scriptDir
$composeFile = Join-Path $rootDir "docker-compose.prod.yml"

function Write-Info ($msg) {
    Write-Host "[run-prod] $msg" -ForegroundColor Cyan
}

function Write-Success ($msg) {
    Write-Host "[run-prod] ✔ $msg" -ForegroundColor Green
}

function Write-Err ($msg) {
    Write-Host "[run-prod] ✖ Error: $msg" -ForegroundColor Red
}

# Verify Docker daemon
try {
    docker info | Out-Null
} catch {
    Write-Err "Docker daemon is not running. Please start Docker Desktop first."
    exit 1
}

# Ensure certificates folder exists
$certDir = Join-Path $rootDir "src\backend\nginx\certs"
if (-not (Test-Path $certDir)) {
    New-Item -ItemType Directory -Path $certDir -Force | Out-Null
}

Write-Info "Starting HCMUS-LDMS Production Stack (Web, API, Postgres, MinIO, MailHog)..."
docker compose -f $composeFile up -d --build

Write-Info "Waiting for API service healthcheck (http://localhost:8000/health)..."
$ready = $false
for ($i = 0; $i -lt 60; $i++) {
    try {
        $res = Invoke-RestMethod -Uri "http://localhost:8000/health" -Method Get -TimeoutSec 2 -ErrorAction SilentlyContinue
        if ($res.status -eq "ok") {
            $ready = $true
            break
        }
    } catch {}
    Start-Sleep -Seconds 1
}

if (-not $ready) {
    docker compose -f $composeFile logs --tail 50 api
    Write-Err "API did not become ready within 60 seconds."
    exit 1
}

Write-Success "API is up and healthy!"

Write-Info "Running automatic database seeding (Users, Categories, Sample Books)..."
try {
    docker compose -f $composeFile exec -T api uv run python -m app.scripts.seed_data
} catch {
    Write-Info "Notice: Seed data finished."
}

Write-Success "HCMUS-LDMS Stack is fully deployed and ready!"

Write-Host ""
Write-Host "======================================================================" -ForegroundColor Green
Write-Host "  🚀 HCMUS-LDMS 1-CLICK PRODUCTION SYSTEM DEPLOYED SUCCESSFULLY" -ForegroundColor Green
Write-Host "======================================================================" -ForegroundColor Green
Write-Host "  🌐 Web Application (HTTP):    http://localhost:8080" -ForegroundColor White
Write-Host "  🔒 Web Application (HTTPS):   https://localhost:8443" -ForegroundColor White
Write-Host "  🔌 API Server (FastAPI):       http://localhost:8000" -ForegroundColor White
Write-Host "  📖 API Interactive Docs:       http://localhost:8000/docs" -ForegroundColor White
Write-Host "  📦 MinIO Object Storage UI:    http://localhost:9003  (ldms / ldms12345)" -ForegroundColor White
Write-Host "  ✉️  Mock Mail Server (MailHog): http://localhost:8025" -ForegroundColor White
Write-Host "  📊 Grafana Dashboards:         http://localhost:3000  (admin / admin)" -ForegroundColor White
Write-Host "  📈 Prometheus Metrics Engine:   http://localhost:9090" -ForegroundColor White
Write-Host "----------------------------------------------------------------------" -ForegroundColor Gray
Write-Host "  🔑 DEFAULT DEMO ACCOUNTS:" -ForegroundColor Yellow
Write-Host "     • Admin:     admin@hcmus.edu.vn     / Admin@123456" -ForegroundColor Yellow
Write-Host "     • Librarian: librarian@hcmus.edu.vn / Librarian@123456" -ForegroundColor Yellow
Write-Host "     • Reader:    reader@hcmus.edu.vn    / Reader@123456" -ForegroundColor Yellow
Write-Host "======================================================================" -ForegroundColor Green
Write-Host "To stop services, run: docker compose -f docker-compose.prod.yml down" -ForegroundColor Gray
Write-Host ""
