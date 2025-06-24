from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .database import get_db
from .models import User
from .schemas import UserRequest, UserResponse

api_v1 = APIRouter(prefix="/api/v1")


@api_v1.get("/")
def root():
    return {"message": "Hello FastAPI + PostgreSQL"}


@api_v1.post("/users/", response_model=UserResponse)
def create_user(user: UserRequest, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
