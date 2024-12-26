from fastapi import FastAPI

from app.api.commentApi import comment_router
from app.api.postApi import post_router
from app.api.commentApi import comment_router
from app.DatabaseConfigs.database import engine,Base




# Create database tables on startup
app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(post_router, prefix="/posts", tags=["posts"])
app.include_router(comment_router,prefix="/comments",tags=["comments"])

