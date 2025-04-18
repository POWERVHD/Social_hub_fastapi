from pydantic import BaseModel, EmailStr, conint
from datetime import datetime
from typing import Optional
from . import models


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    
class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime


class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] | int | None = None
    


class Post(BaseModel):
    title:str
    content:str
    published: bool = True
    owner: UserOut
    

class PostCreate(Post):
    pass

class PostResponse(Post):
    id: int
    created_at: datetime
    owner_id: int


class Vote(BaseModel):
    post_id: int
    dir: conint(ge=0, le=1)


class PostOut(BaseModel):
    Post: Post
    votes: int
