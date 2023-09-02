from flask import Flask, render_template
from flaskext.markdown import Markdown
from database import get_posts, get_post
from typing import Tuple

app = Flask(__name__)
Markdown(app)

@app.route("/")
def index() -> str:
    posts: Tuple[int, str, str] = get_posts() 
    return render_template("index.html", posts=posts)

@app.route("/post/<int:id>")
def post(id) -> (str, int):
    post: Tuple[int, str, str] = get_post(id)
    if post is None:
        return "post not found", 404

    return render_template("post.html", post=post), 200