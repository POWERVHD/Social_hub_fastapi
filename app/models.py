from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime

from sqlalchemy import Column, Boolean, DateTime
from sqlalchemy.sql import expression
from sqlalchemy.sql import func


class Post(SQLModel, table=True):
    __tablename__ = "posts"      # type: ignore

    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(nullable=False)
    content: str = Field(nullable=False)

    published: bool = Field( default=True,
        sa_column=Column(Boolean, server_default=expression.true(), nullable=False)
    )

    created_at: datetime = Field(
    default_factory=datetime.utcnow,
    sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    )

    owner_id: int = Field(foreign_key="users.id",ondelete="CASCADE", nullable=False)

    owner: Optional["User"] = Relationship()

class User(SQLModel, table=True):
    __tablename__ = "users"  # type: ignore
    id: Optional[int] = Field(default=None, primary_key=True)
    email : str = Field(nullable=False, unique=True)
    password: str = Field(nullable=False)

    created_at: datetime = Field(
    default_factory=datetime.utcnow,
    sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    )
    

class Vote(SQLModel, table=True):
    __tablename__ = "votes"
    user_id: int = Field(foreign_key="users.id",ondelete="CASCADE", nullable=False ,primary_key=True)
    post_id: int = Field(foreign_key="posts.id",ondelete="CASCADE", nullable=False ,primary_key=True)
    
