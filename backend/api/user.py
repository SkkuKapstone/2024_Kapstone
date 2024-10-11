from fastapi import APIRouter, Depends
from backend.db.session import get_db, SessionLocal
from backend.schema.models import User
from backend.schema.user.request_models import UserCreateRequest, UserLoginRequest
from backend.schema.user.response_models import UserCreateResponse
from sqlalchemy.orm import Session
import bcrypt

router = APIRouter()

@router.get("/", tags=["User"])
def read_users(db: Session = Depends(get_db)): # GET USERS
    users = db.query(User).all()
    return [{
        "id": user.id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email
    } for user in users]


@router.post("/register", response_model=UserCreateResponse, tags=["User"])
def create_user(user_request: UserCreateRequest, db: Session = Depends(get_db)) -> User: # CREATE USER
    hashed_password = hash_password(user_request.password)  # Hashing
    user = User(
        first_name=user_request.first_name,
        last_name=user_request.last_name,
        email=user_request.email,
        password=hashed_password
    )
    db.add(user)
    db.commit()
    return user



# @router.post("/login", response_model=UserLoginResponse, tags=["User"])
# def login(user_request: UserLoginRequest, db: Session = Depends(get_db)):
#     # is_valid_email(user_request.email)
#     # is_valid_pw()
#     pass

def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')

def is_valid_email(email: str, db: Session = Depends(get_db)):
    pass