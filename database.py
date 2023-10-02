import sqlite3
from typing import Dict, List, Tuple
import settings

DATABASE = settings.DATABASE_PATH

def get_posts() -> List[Dict[str, int | str]]:
    db = sqlite3.connect(DATABASE)
    posts: List[Tuple[int, str, str]] = db.execute("SELECT * FROM post").fetchall()
    db.close()
    return posts

def get_post(id: int) -> Dict[str, int | str]:
    db = sqlite3.connect(DATABASE)
    post: Tuple[int, str, str] = db.execute("SELECT * FROM post WHERE id = ?", (id,)).fetchone()
    db.close()
    return post


class Post:
    pass