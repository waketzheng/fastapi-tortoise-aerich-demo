# fastapi-tortoise-aerich-demo
A demo for using aerich to manage tortoise-orm in fastapi project.

## Create db
- docker
```bash
psql -U postgres -d postgres -c "create database fastapi_tortoise_aerich_demo encoding='utf-8';"
```
- Linux
```
sudo -u postgres psql -U postgres -d postgres -c "create database fastapi_tortoise_aerich_demo encoding='utf-8';"
```
## Install dependencies
```bash
uv sync
source .venv/*/activate
```
## Initial aerich
```bash
aerich init -t app.settings.TORTOISE_ORM
aerich init-db
aerich migrate
aerich upgrade
```
## Start server
```bash
./app/main.py
```
