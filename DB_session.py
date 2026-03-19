import sqlite3

class DbSession:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = None
        self.cursor = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        self.conn.execute("BEGIN")
        return self

    def execute(self, sql, params=None):
        if params is not None:
            self.cursor.execute(sql, params)
        else:
            self.cursor.execute(sql)

    def fetch_all(self, sql, params=None):
        self.execute(sql, params)
        return self.cursor.fetchall()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.conn.rollback()
        else:
            self.conn.commit()
        
        self.conn.close()

# Testing the logic 
if __name__ == "__main__":
    db = "test.sqlite"
    try:
        with DbSession(db) as sess:
            sess.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name TEXT)")
            sess.execute("INSERT INTO users(name) VALUES(?)", ("Bob",))
            print("Force failing transaction...")
            raise RuntimeError("DB Crash!")
    except Exception as e:
        print(f"Caught expected error: {e}")
        
    with DbSession(db) as sess:
        data = sess.fetch_all("SELECT * FROM users")
        print(f"Current users: {data}")