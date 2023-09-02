from io import TextIOWrapper
import sqlite3
import settings

def run_migrations() -> None:
    db: sqlite3.Connection = sqlite3.connect(settings.DATABASE_PATH)
    schema = _get_schema()
    db.cursor().executescript(schema)
    db.close()

def _get_schema() -> str:
    with open(settings.SCHEMA_PATH, "r") as schema_file:
        schema: str = schema_file.read()
    return schema

if __name__ == "__main__":
    run_migrations()