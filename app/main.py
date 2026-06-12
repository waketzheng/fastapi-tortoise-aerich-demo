#!/usr/bin/env python
from pathlib import Path

from asynctor import Timer
from asynctor.contrib.fastapi import add_timing_middleware, config_access_log, runserver
from asynctor.utils import ExtendSyspath
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from loguru import logger
from tortoise.contrib.fastapi import register_tortoise

with ExtendSyspath(BASE_DIR := Path(__file__).parent.parent):
    from app import __version__
    from app.routers.users import router as users_router
    from app.settings import TORTOISE_ORM

app = FastAPI(title=BASE_DIR.name, version=__version__)
config_access_log()
add_timing_middleware(app)
register_tortoise(app, config=TORTOISE_ORM)
app.include_router(users_router, prefix="/users")


@app.get("/")
def homepage() -> HTMLResponse:
    with Timer("Generate home page") as t:
        docs = "<a href='/docs'>docs</a>"
        html = f"<h1>Hello from fastapi-tortoise-aerich-demo!</h1>{docs}"
        response = HTMLResponse(html)
    logger.debug(t)
    return response


if __name__ == "__main__":
    runserver(app, reload=True)
