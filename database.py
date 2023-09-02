import sqlite3
from sqlite3 import Connection, Cursor
from typing import Dict, List
from flask import g
import settings

DATABASE = settings.DATABASE_PATH

def init_db() -> None:
    db = sqlite3.connect(DATABASE)
    _run_migrations(db)
    db.close()

def get_posts() -> List[Dict[str, int | str]]:
    db = sqlite3.connect(DATABASE)
    posts: List[Dict[str, int | str]] = db.execute("SELECT * FROM posts").fetchall()
    db.close()
    return posts

def _run_migrations(db: Connection) -> None:
    schema_file: str = open("./schema.sql", "r")
    schema = schema_file.read()
    schema_file.close()
    db.cursor().executescript(schema)
