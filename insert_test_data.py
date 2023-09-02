import sqlite3
import settings

def insert_test_data() -> None:
    db: sqlite3.Connection = sqlite3.connect(settings.DATABASE_PATH)
    schema = _get_test_data_schema()
    db.cursor().executescript(schema)
    db.close()

def _get_test_data_schema() -> str:
    with open(settings.TEST_DATA_SCHEMA_PATH, "r") as schema_file:
        schema: str = schema_file.read()
    return schema

if __name__ == "__main__":
    insert_test_data()