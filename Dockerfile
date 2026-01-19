FROM python:3.12

COPY ./certs/homelab-root-ca-bundle.pem ./certs/homelab-root-ca-bundle.pem
RUN cat /etc/ssl/certs/ca-certificates.crt ./certs/homelab-root-ca-bundle.pem > /etc/ssl/certs/ca-bundle.pem
ENV SSL_CERT_FILE=/etc/ssl/certs/ca-bundle.pem
ENV REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-bundle.pem
RUN pip install poetry

WORKDIR /app-root
COPY . /app-root


RUN poetry install --only main

CMD ["poetry", "run", "python", "-m", "app.main"]