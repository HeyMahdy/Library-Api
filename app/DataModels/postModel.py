from sqlalchemy import  Integer, String, ForeignKey
from sqlalchemy.orm import mapped_column, relationship, Mapped
from typing import List
from pydantic import BaseModel, ConfigDict

from app.DataModels.commentModel import Comment
from app.DatabaseConfigs.database import Base

class Post(Base):

    __tablename__ = 'posts'
    id : Mapped[int] = mapped_column(Integer, primary_key=True,index=True,autoincrement=True)
    title : Mapped[str] = mapped_column(String,nullable=False)
    description : Mapped[str] = mapped_column(String,nullable=False)
    comments: Mapped[List["Comment"]] = relationship("Comment", cascade="all, delete-orphan")



class PostCreate(BaseModel):
    title : str
    description : str
    model_config = ConfigDict(from_attributes=True)

class PostResponse(BaseModel):

    title: str
    description: str
    model_config = ConfigDict(from_attributes=True)