import sqlite3

conn = sqlite3.connect("database_posts.db")
cursor = conn.cursor()
def posts():
    text = """CREATE TABLE IF NOT EXISTS ACCOUNTS (
    post_id INT IDENTITY(1, 1),
    host_name TEXT,
    host_family_name TEXT,
    city TEXT,
    address TEXT,
    content TEXT,
    date TEXT,
    SPOTS INTEGER,
    availbale INTEGER
    )"""
    cursor.execute(text)

