from flask import Flask, render_template
from database import init_db, get_posts
from typing import List

app = Flask(__name__)

init_db()

@app.route("/")
def index() -> str:
    #posts: List[Post] = Posts.get()
    posts = get_posts() 
    return render_template("index.html", posts=posts)

"""
@app.route("/post/<int:id>")
def post(id) -> (str, int):
    post: Post | None = Posts.get_id(id)
    if post is None:
        return "post not found", 404

    return render_template("post.html", post=post), 200
"""