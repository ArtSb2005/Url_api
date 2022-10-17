import sqlite3

class Database:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def add_user(self, url: str):
        with self.conn:
            self.cursor.execute("""INSERT INTO urls (url) VALUES (?)""",
                                (url,))

