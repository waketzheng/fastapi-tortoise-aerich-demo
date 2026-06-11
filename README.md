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
just deps
```
## Initial aerich
```bash
pdm run aerich init -t app.settings.TORTOISE_ORM
pdm run aerich init-db
pdm run aerich migrate
pdm run aerich upgrade
```
## Start server
```bash
just dev
```
