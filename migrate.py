from io import TextIOWrapper
import sqlite3
import settings

def run_migrations() -> None:
    db: sqlite3.Connection = sqlite3.connect(settings.DATABASE_PATH)
    schema = _get_schema()
    db.cursor().executescript(schema)
    db.close()

def _get_schema() -> str:
    schema_file: TextIOWrapper = open(settings.SCHEMA_PATH, "r")
    schema: str = schema_file.read()
    schema_file.close()
    return schema

if __name__ == "__main__":
    run_migrations()