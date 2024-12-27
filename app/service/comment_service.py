from sqlalchemy.orm import Session
from app.DataModels.commentModel import Comment, CommentModel
from app.DataModels.postModel import Post
from app.DataModels.ResponseModel import SuccessResponse



def create_comment(comment: CommentModel,post_id:int,db:Session):
    post = db.query(Post).filter(Post.id == post_id).first()
    if post is None:
        return SuccessResponse(status="Error",message="Post not found")
    else:
        new_comment = Comment(text=comment.text,post_id=post_id)
        post.comments.append(new_comment)
        db.add(new_comment)
        db.commit()
        db.refresh(new_comment)
        return SuccessResponse(status="Success",message="Comment created successfully")


def get_all_comments(post_id:int,db:Session):
        comments = db.query(Comment).filter(Comment.post_id == post_id).all()
        if comments is None:
            return SuccessResponse(status="Error",message="Comments not found")
        else:
            return SuccessResponse(status="Success",message="Comments found successfully")




