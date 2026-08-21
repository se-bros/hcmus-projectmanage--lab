FROM node:20-slim AS frontend-build
WORKDIR /frontend
COPY src/frontend/package*.json ./
RUN npm ci
COPY src/frontend ./
RUN npm run build

FROM nginx:1.24-alpine
RUN apk add --no-cache openssl && \
    mkdir -p /etc/nginx/certs && \
    openssl req -x509 -nodes -newkey rsa:2048 \
      -keyout /etc/nginx/certs/dev.key \
      -out /etc/nginx/certs/dev.crt \
      -days 365 \
      -subj "/CN=localhost" \
      -addext "subjectAltName=DNS:localhost"

COPY src/backend/nginx/nginx.conf /etc/nginx/nginx.conf
COPY --from=frontend-build /frontend/dist /usr/share/nginx/html
EXPOSE 80 443
