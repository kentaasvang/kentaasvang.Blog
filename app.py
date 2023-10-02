from flask import Flask, render_template
from database import get_posts, get_post
from typing import Tuple

from models import PostModel

app = Flask(__name__)


@app.route("/")
def index() -> str:
    posts = get_posts()
    posts = [PostModel(*post) for post in posts]
    return render_template("index.html", posts=posts)

@app.route("/post/<int:id>")
def post(id) -> (str, int):
    post = get_post(id)
    post = PostModel(*post)
    if post is None:
        return "post not found", 404

    return render_template("post.html", post=post)