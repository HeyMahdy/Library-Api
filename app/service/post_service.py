from sqlalchemy.orm import Session
from app.DataModels.postModel import Post


def get_all_posts(db:Session):
    posts = db.query(Post).all()
    return posts


def create_post(post:Post,db:Session):
    new_post = Post(title=post.title,description=post.description)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


def delete_post(post_id:int,db:Session):
    post = db.query(Post).filter(Post.id == post_id).first()
    if post is None:
        return {"message": "Post not found"}
    else:
     db.delete(post)
     db.commit()
    return {"message": "Post deleted successfully"}


def update_post(post_id:int,post:Post,db:Session):
    post_to_update = db.query(Post).filter(Post.id == post_id).first()
    if post_to_update is None:
        return {"message": "Post not found"}
    else:
        post_to_update.title = post.title
        db.commit()
        return {"message": "Post updated successfully"} 


def find_post(post_id:int,db:Session):
    post = db.query(Post).filter(Post.id == post_id).first()
    return post