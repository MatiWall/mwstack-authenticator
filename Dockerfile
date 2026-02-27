FROM node:25.7.0-alpine AS frontend-builder


WORKDIR /frontend

COPY frontend/package*.json ./
RUN npm install

COPY frontend ./

RUN npm run build

FROM python:3.12-slim AS python-builder

WORKDIR /app-root

COPY app ./app
COPY alembic.ini ./alembic.ini
COPY appconfig.yaml ./appconfig.yaml
COPY poetry.lock ./poetry.lock
COPY pyproject.toml ./pyproject.toml
COPY secrets.yaml ./secrets.yaml 
COPY README.md ./README.md
# Temp


COPY ./certs/homelab-root-ca-bundle.pem ./certs/homelab-root-ca-bundle.pem
RUN cat /etc/ssl/certs/ca-certificates.crt ./certs/homelab-root-ca-bundle.pem > /etc/ssl/certs/ca-bundle.pem
ENV SSL_CERT_FILE=/etc/ssl/certs/ca-bundle.pem
ENV REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-bundle.pem

RUN pip install poetry

RUN poetry export -f requirements.txt --without-hashes -o requirements.txt

RUN apt-get update && \ 
   apt-get install -y libpq-dev gcc

RUN poetry bundle venv --only main /venv

FROM python:3.12-slim AS base
WORKDIR /app-root

COPY --from=frontend-builder frontend/dist ./frontend/dist
COPY --from=python-builder requirements.txt ./requirements.txt

#RUN apt-get update && \ 
#   apt-get install -y libpq-dev gcc

# no need for poetry
RUN pip install --no-cache-dir --user -r requirements.txt

CMD ["python", "-m", "app.main"]