from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from .database import get_db
from .models import User
from .schemas import UserRequest, UserResponse
from .logging_config import get_logger

api_v1 = APIRouter(prefix="/api/v1")
logger = get_logger(__name__)


@api_v1.get("/")
def root():
    logger.info("Root endpoint accessed")
    return {"message": "Hello FastAPI + PostgreSQL"}


@api_v1.post("/users/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserRequest, db: Session = Depends(get_db)):
    logger.info("Creating new user", email=user.email, name=user.name)

    try:
        existing_user = db.query(User).filter(User.email == user.email).first()
        if existing_user:
            logger.warning("User creation failed - email already exists", email=user.email)
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already registered")

        new_user = User(**user.model_dump())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        logger.info("User created successfully", user_id=new_user.id, email=new_user.email)
        return new_user

    except HTTPException as e:
        raise e

    except SQLAlchemyError as e:
        db.rollback()
        logger.error("Database error during user creation", error=str(e), email=user.email)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to create user due to database error"
        )
    except Exception as e:
        db.rollback()
        logger.error("Unexpected error during user creation", error=str(e), email=user.email)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An unexpected error occurred")
