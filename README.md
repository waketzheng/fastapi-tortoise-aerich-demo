# fastapi-tortoise-aerich-demo
A demo for using aerich to manage tortoise-orm in fastapi project.

## Create db
- docker
```bash
psql -U postgres -d postgres -c "create database fastapi_tortoise_aerich_demo encoding='utf-8';"
```
- system service
```
sudo -u postgres psql -U postgres -d postgres -c "create database fastapi_tortoise_aerich_demo encoding='utf-8';"
```
## Install dependencies
```bash
uv python pin 3.11
uv sync
```
## Initial aerich
```bash
source .venv/*/activate
aerich init -t app.settings.TORTOISE_ORM
aerich init-db
aerich migrate
aerich upgrade
```
## Start server
```bash
./app/main.py
```
