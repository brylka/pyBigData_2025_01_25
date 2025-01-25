import random
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI
import uvicorn

app = FastAPI()

DB_URL = "mysql+mysqlconnector://root:@localhost/posts"
engine = create_engine(DB_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True, index=True)
    author = Column(String(100))
    content = Column(String(500))
    date = Column(DateTime, default=datetime.now)

Base.metadata.create_all(bind=engine)

@app.get("/posts/{post_id}")
def get_post(post_id: int):
    db = SessionLocal()
    post = db.query(Post).filter(Post.id == post_id).first()
    db.close()

    if post:
        return {
            "id": post.id,
            "author": post.author,
            "content": post.content,
            "date": str(post.date)
        }
    return {"error": "Post not found"}

@app.get("/posts")
def get_all_posts():
    db = SessionLocal()
    posts = db.query(Post).all()
    db.close()
    # response = []
    # for post in posts:
    #     j = {"id": post.id, "author": post.author, "content": post.content, "date": str(post.date)}
    #     response.append(j)

    response = [{"id": post.id, "author": post.author, "content": post.content, "date": str(post.date)} for post in posts]

    return response



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)