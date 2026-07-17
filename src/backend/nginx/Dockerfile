FROM node:20-slim AS frontend-build
WORKDIR /frontend
COPY src/frontend/package*.json ./
RUN npm ci
COPY src/frontend ./
RUN npm run build

FROM nginx:1.24-alpine
COPY src/backend/nginx/nginx.conf /etc/nginx/nginx.conf
COPY --from=frontend-build /frontend/dist /usr/share/nginx/html
EXPOSE 80 443
