from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api_v1 import api_v1
from app.database import engine, Base


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(api_v1)
