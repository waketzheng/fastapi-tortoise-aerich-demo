from pathlib import Path
from urllib.parse import quote_plus


def auto_load(strict=False) -> list[str]:
    parent = Path(__file__).parent
    if parent.joinpath("models.py").exists():
        return ["app.models"]
    models_dir = Path(parent, "models")
    if not models_dir.exists():
        raise RuntimeError("models.py and models/ not found!")
    files = [p for p in models_dir.glob("*.py") if p.name[0] != "_"]
    if strict:
        files = [p for p in files if b"tortoise" in p.read_bytes()]
    return [f"app.models.{p.stem}" for p in files]


DB_NAME = "fastapi_tortoise_aerich_demo"
DB_PASSWORD = quote_plus("postgres")
DB_URL = f"postgres://postgres:{DB_PASSWORD}@127.0.0.1:5432/{DB_NAME}"
TORTOISE_ORM = {
    "connections": {"default": DB_URL},
    "apps": {"models": {"models": [*auto_load(), "aerich.models"]}},
}
