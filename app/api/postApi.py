from fastapi import HTTPException
from typing import List
from app.DataModels.postModel import PostCreate , PostResponse
from fastapi import APIRouter
from app.DatabaseConfigs.database import SessionDep
from app.service.post_service import  get_all_posts , create_post , find_post , delete_post , update_post



post_router = APIRouter()


@post_router.post("/posts/", response_model=PostResponse)
async def create_pppost(post: PostCreate, db: SessionDep):
    new_post = create_post(post,db)
    return new_post

@post_router.get("/all/", response_model=List[PostResponse])
async def all_posts(db: SessionDep):
    posts = get_all_posts(db)
    if not posts:
        raise HTTPException(status_code=404, detail="Posts not found")
    return posts

@post_router.get("/create/{post_id}",response_model=PostResponse)
async def get_post(post_id:int , db : SessionDep):
    post = find_post(post_id,db)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@post_router.delete("/delete/{post_id}")
async def delete_POST(post_id:int , db : SessionDep):
      string = delete_post(post_id,db)
      return string


@post_router.put("/update_post/{post_id}")
async def update_POST(post_id:int , post: PostCreate , db : SessionDep):
     string = update_post(post_id,post,db)
     return string