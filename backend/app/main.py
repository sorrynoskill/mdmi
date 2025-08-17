from fastapi import FastAPI

from .core.config import settings

app = FastAPI()


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/config")
def get_config() -> dict[str, str]:
    return settings.model_dump()
