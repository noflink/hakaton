import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()


def start_soldiers_db():
    text = """CREATE TABLE IF NOT EXISTS GUESTS (
    guest_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    family_name TEXT,
    email TEXT UNIQUE,
    password TEXT
    )"""
    cursor.execute(text)


def start_hosts_db():
    text = """CREATE TABLE IF NOT EXISTS HOSTS (
    host_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    family_name TEXT,
    email TEXT UNIQUE,
    password TEXT,
    id INTEGER,
    address TEXT,
    phone_number INTEGER
    )"""
    cursor.execute(text)


def add_guest(name, family, email, password):  # can be changed into an object class (simpler probably)
    text = """INSERT INTO GUESTS (name, family_name, email, password)
    VALUES (?,?,?,?)"""

    cursor.execute(text, (name, family, email, password))
    conn.commit()


def add_host(name, family, email, password, id, address, phone):
    text = """INSERT INTO HOSTS (name, family_name, email, password, id, address, phone_number)
    VALUES (?,?,?,?,?,?,?)"""

    cursor.execute(text, (name, family, email, password, id, address, phone))
    conn.commit()

