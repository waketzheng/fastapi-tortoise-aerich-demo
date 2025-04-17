#!/usr/bin/env python
import uvicorn
from fastapi import FastAPI
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

app = FastAPI()
register_tortoise(app, config=TORTOISE_ORM)


@app.get("/")
def main():
    return "Hello from fastapi-tortoise-aerich-demo!"


if __name__ == "__main__":
    uvicorn.run(app)
