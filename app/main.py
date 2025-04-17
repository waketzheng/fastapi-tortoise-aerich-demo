#!/usr/bin/env python
import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from tortoise.contrib.fastapi import register_tortoise

try:
    from app.settings import TORTOISE_ORM
except ImportError as e:
    if "No module named 'app'" in str(e):
        import sys
        from pathlib import Path

        _workdir = Path(__file__).parent.parent.as_posix()
        if _workdir not in sys.path:
            sys.path.append(_workdir)
        from app.settings import TORTOISE_ORM
    else:
        raise e
from app.routers.users import router as users_router

app = FastAPI()
register_tortoise(app, config=TORTOISE_ORM)
app.include_router(users_router, prefix="/users")


@app.get("/")
def main():
    docs = "<a href='/docs'>docs</a>"
    return HTMLResponse(f"<h1>Hello from fastapi-tortoise-aerich-demo!</h1>{docs}")


if __name__ == "__main__":
    uvicorn.run(app)
