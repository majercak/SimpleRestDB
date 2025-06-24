from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api_v1 import api_v1
from app.database import engine, Base
from app.logging_config import configure_logging, get_logger

logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    configure_logging()
    logger.info("Application starting up")
    Base.metadata.create_all(bind=engine)
    yield
    logger.info("Application shutting down")


app = FastAPI(lifespan=lifespan)
app.include_router(api_v1)
