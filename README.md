## Create db
- docker
```bash
psql -U postgres -d postgres -c "create database fastapi_tortoise_aerich_demo encoding='utf-8';"
```
- Linux
```
sudo -u postgres psql -U postgres -d postgres -c "create database fastapi_tortoise_aerich_demo encoding='utf-8';"
```
## Initial aerich
```bash
aerich init -t app.settings.TORTOISE_ORM
aerich init-db
```
