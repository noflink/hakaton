import sqlite3
import consts

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
    content TEXT,
    date TEXT
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

    temp = []

    text = """SELECT * FROM POSTS WHERE post_id=?"""
    for id in ids:
        cursor.execute(text, (id[0],))
        temp.append(cursor.fetchone())

    posts = turn_to_dict(temp)
    return posts


def get_host_posts(host_id):
    text = """SELECT * FROM POSTS WHERE host_id=?"""
    cursor.execute(text, (host_id,))
    temp = cursor.fetchall()
    posts = turn_to_dict(temp)
    return posts


def start():
    start_guests_db()
    start_posts_db()
    start_hosts_db()


def check_sing_up_email(email, usertype):
    text = f"SELECT user_id FROM {usertype} WHERE email=?"
    cursor.execute(text, (email,))

    if cursor.fetchone()[0] is not None:
        return False
    return True

def check_login(email, password, usertype):
    text = f"SELECT password FROM {usertype} WHERE email=?"
    cursor.execute(text, (email,))

    if cursor.fetchone()[0] != password:
        return False
    return True

def get_all_posts():
    text = f"SELECT * FROM POSTS"
    cursor.execute(text)
    temp = cursor.fetchall()
    posts = turn_to_dict(temp)
    return posts

def turn_to_dict(posts):
    res = []
    for item in posts:
        post = {"post_id": item[0],
                "host_id": item[1],
                "host_name": item[2],
                "host_family": item[3],
                "city": item[4],
                "address": item[5],
                "spots": item[6],
                "available": item[7],
                "content": item[8],
                "date" : item[9]}
        res.append(post)

    return res
