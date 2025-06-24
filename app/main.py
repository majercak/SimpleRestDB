from fastapi import FastAPI
from . import models
from .database import engine

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)


@app.get("/")
async def root():
    return {"message": "Hello async FastAPI + PostgreSQL"}
