#!/usr/bin/env python
from pathlib import Path

from asynctor.contrib.fastapi import runserver
from asynctor.utils import ExtendSyspath
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from tortoise.contrib.fastapi import register_tortoise

with ExtendSyspath(Path(__file__).parent.parent):
    from app.routers.users import router as users_router
    from app.settings import TORTOISE_ORM

app = FastAPI()
register_tortoise(app, config=TORTOISE_ORM)
app.include_router(users_router, prefix="/users")


@app.get("/")
def homepage() -> HTMLResponse:
    docs = "<a href='/docs'>docs</a>"
    return HTMLResponse(f"<h1>Hello from fastapi-tortoise-aerich-demo!</h1>{docs}")


if __name__ == "__main__":
    runserver(app, reload=True)
