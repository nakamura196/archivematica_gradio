# Archivematica Gradio

A demonstration of Archivematica and Gradio.

<img src="assets/demo.gif" width="100%" title="Demo">

## 🌐 Website

[Visit the demo page](https://amg.aws.ldas.jp/) to try it out.

## Preparation

`src/.env` and `docker-compose-prod.yml` are required.

```src/.env
DASHBOARD_URL=http://localhost:62080
DASHBOARD_USERNAME=test
DASHBOARD_API_KEY=test

STORAGE_SERVICE_URL=http://localhost:62081
STORAGE_SERVICE_USERNAME=test
STORAGE_SERVICE_PASSWORD=test

AWS_ACCESS_KEY_ID=xxxxxxxxxxxxxxxxxxxx
AWS_SECRET_ACCESS_KEY=xxxxxxxxxxxxxxxxxxxx
```

```docker-compose-prod.yml
version: "3.0"

services:
  gradio:
    container_name: "archivematica_gradio"
    build: .
    volumes:
      - ./src:/workspace
    ports:
      - "7865:7860"
    environment:
      VIRTUAL_HOST: xxx
      LETSENCRYPT_HOST: xxx
      LETSENCRYPT_EMAIL: xxx

networks:
  default:
    external:
      name: xxx
```

## 📖 Installation

```bash
docker compose up --build
```

## Production

```bash
docker compose -f docker-compose-prod.yml up -d
```
