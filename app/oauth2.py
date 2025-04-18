from fastapi import Depends, status, HTTPException, Response
import jwt
from jwt.exceptions import PyJWTError
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta, timezone
from . import schemas, models
from .database import get_session
from sqlmodel import Session, select
from .config import settings




oauth2_schema = OAuth2PasswordBearer(tokenUrl='login')



SECRET_KEY = f"{settings.secret_key}"
ALGORITHM = f"{settings.algorithm}"
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes

def create_access_token(data: dict):       # Since it is a payload so its a dict
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES) # abhi ke current time se 30 min tak
    to_encode.update({"exp":expire})

    encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)

    return encoded_jwt

def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        id = payload.get("user_id")

        if id is None:
            raise credentials_exception
        token_data = schemas.TokenData(id=id)

    except PyJWTError:
        raise credentials_exception
    
    return token_data

def get_current_user(token: str = Depends(oauth2_schema), db: Session = Depends(get_session)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    token_data = verify_access_token(token, credentials_exception)

    user = db.exec(select(models.User).where(models.User.id == token_data.id)).first()
 
    return user


