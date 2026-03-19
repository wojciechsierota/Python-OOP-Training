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

# --- Testing the logic ---
try:
    with DbSession("mydb.sqlite") as session:
        session.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name TEXT)")
        session.execute("INSERT INTO users(name) VALUES(?)", ("Bob",))
        print("Attempting to add Bob to the database...")
        raise Exception("Sudden system failure!") 
except Exception as e:
    print(f"Caught an error: {e}")

with DbSession("mydb.sqlite") as session:
    users = session.fetch_all("SELECT * FROM users")
    print(f"Users in database after failure: {users}")

print("Done")