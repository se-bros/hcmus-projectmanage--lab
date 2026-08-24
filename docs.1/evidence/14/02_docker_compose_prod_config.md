# BẢN IN CẤU HÌNH HẠ TẦNG DOCKER COMPOSE PRODUCTION

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

---

### THÔNG TIN TỆP NGUỒN (FILE CONTROL)

| Trường thông tin                 | Nội dung chi tiết                                                                                                                                                      |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Tên tệp tin (File Name):**     | `docker-compose.prod.yml`                                                                                                                                              |
| **Đường dẫn trong Repo (Path):** | `docker-compose.prod.yml`                                                                                                                                              |
| **Công nghệ:**                   | Docker Compose v2 (Multi-container Orchestration)                                                                                                                      |
| **Mục đích:**                    | Định nghĩa toàn bộ hạ tầng vận hành: Reverse Proxy Nginx (TLS 8443), Frontend React, Backend FastAPI, CSDL PostgreSQL, Lưu trữ MinIO S3, Giám sát Prometheus & Grafana |

---

## 1. Danh mục các dịch vụ cấu hình (Services Architecture)

1. **`nginx`**: Cổng đón tiếp HTTP (cổng 8080) và HTTPS (cổng 8443), định tuyến traffic tới Frontend và Backend.
2. **`web`**: Giao diện người dùng React/Next.js phục vụ độc giả và thủ thư.
3. **`api`**: Máy chủ backend FastAPI xử lý OCR, trích xuất metadata và quản lý phân quyền RBAC.
4. **`postgres`**: Cơ sở dữ liệu quan hệ PostgreSQL 16 lưu trữ người dùng, mục lục và siêu dữ liệu.
5. **`minio`**: Kho lưu trữ đối tượng S3-compatible lưu trữ tệp scan gốc và tệp sách điện tử EPUB.
6. **`prometheus` & `grafana`**: Hệ thống thu thập metrics và giám sát hiệu năng trực quan.

---

## 2. Toàn văn cấu hình `docker-compose.prod.yml`

```yaml
services:
  web:
    build:
      context: .
      dockerfile: src/backend/nginx/Dockerfile
    ports:
      - "8080:80"
      - "8443:443"
    volumes:
      - ./src/backend/nginx/certs:/etc/nginx/certs:ro
    depends_on:
      - api
    restart: unless-stopped

  api:
    build:
      context: src/backend
      dockerfile: Dockerfile
    ports:
      - "8000:8000"
    environment:
      APP_ENV: ${APP_ENV:-production}
      DATABASE_URL: postgresql+psycopg://${POSTGRES_USER:-ldms}:${POSTGRES_PASSWORD:-ldms}@postgres:5432/${POSTGRES_DB:-ldms}
      MINIO_ENDPOINT: minio:9000
      MINIO_ACCESS_KEY: ${MINIO_ROOT_USER:-ldms}
      MINIO_SECRET_KEY: ${MINIO_ROOT_PASSWORD:-ldms12345}
      MINIO_BUCKET: ${MINIO_BUCKET:-ldms}
      MINIO_SECURE: ${MINIO_SECURE:-false}
      CORS_ORIGINS: '["http://localhost", "https://localhost", "http://localhost:8080", "https://localhost:8443", "http://localhost:5173", "https://hcmus-projectmanage-lab.vercel.app"]'
      OCR_DPI: ${OCR_DPI:-300}
      OCR_LANGUAGE: ${OCR_LANGUAGE:-vie+eng}
      OCR_TIMEOUT_SECONDS: ${OCR_TIMEOUT_SECONDS:-60}
      PDF_RENDER_TIMEOUT_SECONDS: ${PDF_RENDER_TIMEOUT_SECONDS:-120}
      PANDOC_TIMEOUT_SECONDS: ${PANDOC_TIMEOUT_SECONDS:-120}
      ENABLE_MOCK_AUTH: ${ENABLE_MOCK_AUTH:-true}
      JWT_SECRET: ${JWT_SECRET:-dev-insecure-secret-change-me-min-32-bytes}
      JWT_ALGORITHM: ${JWT_ALGORITHM:-HS256}
      JWT_EXPIRES_MINUTES: ${JWT_EXPIRES_MINUTES:-1440}
      GOOGLE_CLIENT_ID: ${GOOGLE_CLIENT_ID:-}
      GOOGLE_CLIENT_SECRET: ${GOOGLE_CLIENT_SECRET:-}
      GOOGLE_REDIRECT_URI: ${GOOGLE_REDIRECT_URI:-}
      GOOGLE_ALLOWED_DOMAINS: ${GOOGLE_ALLOWED_DOMAINS:-[]}
      FRONTEND_BASE_URL: ${FRONTEND_BASE_URL:-http://localhost:8080}
      SMTP_HOST: ${SMTP_HOST:-mailhog}
      SMTP_PORT: ${SMTP_PORT:-1025}
      AUTO_SEED_DATA: ${AUTO_SEED_DATA:-true}
    depends_on:
      postgres:
        condition: service_healthy
      minio:
        condition: service_healthy
    restart: unless-stopped

  postgres:
    image: postgres:16
    environment:
      POSTGRES_USER: ${POSTGRES_USER:-ldms}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD:-ldms}
      POSTGRES_DB: ${POSTGRES_DB:-ldms}
    ports:
      - "5434:5432"
    volumes:
      - postgres_prod_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER:-ldms}"]
      interval: 5s
      timeout: 5s
      retries: 5
    restart: unless-stopped

  minio:
    image: minio/minio:latest
    command: server /data --console-address ":9001"
    environment:
      MINIO_ROOT_USER: ${MINIO_ROOT_USER:-ldms}
      MINIO_ROOT_PASSWORD: ${MINIO_ROOT_PASSWORD:-ldms12345}
    ports:
      - "9002:9000"
      - "9003:9001"
    volumes:
      - minio_prod_data:/data
    healthcheck:
      test: ["CMD", "mc", "ready", "local"]
      interval: 5s
      timeout: 5s
      retries: 5
    restart: unless-stopped

  mailhog:
    image: mailhog/mailhog:latest
    ports:
      - "1025:1025"
      - "8025:8025"
    restart: unless-stopped

  prometheus:
    image: prom/prometheus:latest
    volumes:
      - ./monitoring/prometheus/prometheus.yml:/etc/prometheus/prometheus.yml:ro
    ports:
      - "9090:9090"
    restart: unless-stopped

  grafana:
    image: grafana/grafana:latest
    environment:
      - GF_SECURITY_ADMIN_USER=admin
      - GF_SECURITY_ADMIN_PASSWORD=admin
      - GF_USERS_ALLOW_SIGN_UP=false
    volumes:
      - ./monitoring/grafana/provisioning/datasources:/etc/grafana/provisioning/datasources:ro
      - ./monitoring/grafana/provisioning/dashboards:/etc/grafana/provisioning/dashboards:ro
      - ./monitoring/grafana/dashboards:/etc/grafana/provisioning/dashboards/json:ro
      - grafana_prod_data:/var/lib/grafana
    ports:
      - "3000:3000"
    depends_on:
      - prometheus
    restart: unless-stopped

volumes:
  postgres_prod_data:
  minio_prod_data:
  grafana_prod_data:
```
