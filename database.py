import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()


def start_guests_db():
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

def start_posts_db():
    text = """CREATE TABLE IF NOT EXISTS POSTS (
    post_id INTEGER PRIMARY KEY AUTOINCREMENT,
    host_id TEXT,
    host_name TEXT,
    host_family TEXT,
    city TEXT,
    address TEXT,
    spots INTEGER,
    available INTEGER,
    CONTENT TEXT
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


def add_post(host_id, host_name, host_family, city, address, spots, content):
    text = """INSERT INTO POSTS (host_id, host_name, host_family, city, address, spots, available, content)
    VALUES (?,?,?,?,?,?,?,?)"""
    cursor.execute(text, (host_id, host_name, host_family, city, address, spots, spots, content))
    conn.commit()

def get_posts(city):
    text = """SELECT post_id FROM POSTS WHERE city=?"""
    cursor.execute(text, (city,))
    ids = cursor.fetchall()
    print(ids)

    posts = []

    text = """SELECT * FROM POSTS WHERE post_id=?"""
    for id in ids:
        cursor.execute(text, (id[0],))
        posts.append(cursor.fetchone())

    return posts

def get_host_posts(host_id):
    text = """SELECT * FROM POSTS WHERE host_id=?"""
    cursor.execute(text, (host_id,))
    return cursor.fetchall()
