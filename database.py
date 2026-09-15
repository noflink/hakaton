import sqlite3


conn = sqlite3.connect("database.db")
cursor = conn.cursor()
def start_soldiers_db():
    text = """CREATE TABLE IF NOT EXISTS ACCOUNTS (
    user_id INT IDENTITY(1, 1),
    name TEXT,
    family_name TEXT,
    email TEXT UNIQUE,
    password TEXT
    )"""
    cursor.execute(text)
