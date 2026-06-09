from fastapi import APIRouter
from pydantic import BaseModel

from auth.login import login_user
from auth.register import register_user

from database.postgres import SessionLocal

router = APIRouter()


class RegisterRequest(BaseModel):

    name: str
    email: str
    password: str


class LoginRequest(BaseModel):

    email: str
    password: str


@router.post("/register")
def register(data: RegisterRequest):

    db = SessionLocal()

    result = register_user(
        db,
        data.name,
        data.email,
        data.password
    )

    return result


@router.post("/login")
def login(data: LoginRequest):

    db = SessionLocal()

    result = login_user(
        db,
        data.email,
        data.password
    )

    return result