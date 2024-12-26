from sqlalchemy import  Integer, String, ForeignKey
from sqlalchemy.orm import mapped_column, relationship, Mapped
from typing import List
from pydantic import BaseModel, ConfigDict
from app.DatabaseConfigs.database import Base



class Comment(Base):
    __tablename__ = 'comment'
    id : Mapped[int] = mapped_column(Integer, primary_key=True,index=True,autoincrement=True)
    text : Mapped[str] = mapped_column(String,nullable=False)
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id", ondelete="CASCADE"), nullable=False)

    # Relationships




class CommentModel(BaseModel):
    text : str
    model_config = ConfigDict(from_attributes=True)



class CommentResponse(BaseModel):
    text : str
    model_config = ConfigDict(from_attributes=True)

 
