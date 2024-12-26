from fastapi import HTTPException
from typing import List

from app.DataModels import ResponseModel
from app.DataModels.ResponseModel import SuccessResponse
from app.DataModels.commentModel import CommentModel
from app.DataModels.postModel import PostCreate , PostResponse
from fastapi import APIRouter
from app.DatabaseConfigs.database import SessionDep
from app.service.comment_service import  get_all_comments , create_comment


comment_router = APIRouter()


@comment_router.get("/all/{post_id}",response_model=SuccessResponse)
async def all_comments(post_id:int,db: SessionDep):
    comments = get_all_comments(post_id,db)
    return comments

@comment_router.post("/create/{post_id}", response_model=SuccessResponse)
async def create_Ccomment(comment: CommentModel, post_id: int, db: SessionDep):
    return create_comment(comment,post_id,db)




## why use same function anmeeeeee