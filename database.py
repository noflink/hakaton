import sqlite3


conn = sqlite3.connect("database.db")
cursor = conn.cursor()
def start_soldiers_db():
    text = """CREATE TABLE IF NOT EXISTS GUESTS (
    guest_id INT IDENTITY(1, 1),
    name TEXT,
    family_name TEXT,
    email TEXT UNIQUE,
    password TEXT
    )"""
    cursor.execute(text)

def start_hosts_db():
    text = """CREATE TABLE IF NOT EXISTS HOSTS (
    host_id INT IDENTITY(1,1),
    name TEXT,
    family_name TEXT,
    email TEXT UNIQUE,
    password TEXT,
    id INT,
    address TEXT,
    phone_number INT
    )"""
    cursor.execute(text)
#
# start_hosts_db()
# start_soldiers_db()