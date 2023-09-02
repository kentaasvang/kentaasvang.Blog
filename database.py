from typing import Dict, List, Any

database: Dict[str, List[Any]] = {
    "posts": []
}

def init_db() -> None:
    database["posts"].append({
        "id": 1,
        "title": "First post",
        "body": "This is my first post"
    })
    database["posts"].append({
        "id": 2,
        "title": "Second post",
        "body": "This is my second post"
    })
    database["posts"].append({
        "id": 3,
        "title": "Third post",
        "body": "This is my third post"
    })


class Post:
    def __init__(self, id: int, title: str, body: str):
        self.id = id
        self.title = title
        self.body = body

class Posts:
    @staticmethod
    def get() -> List[Post]:
        posts: List[Dict[str, int | str]] = database["posts"]
        ret_val = []
        for post in posts:
            ret_val.append(Post(**post))
        return ret_val

    @staticmethod
    def get_id(id: int) -> Post | None:
        posts: List[Dict[str, int | str]] = database["posts"]
        for post in posts:
            if post["id"] == id:
                return Post(**post)
        return None