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
    phone_number INTEGER,
    city TEXT
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


def add_host(name, family, email, password, id, address, phone, city):
    text = """INSERT INTO HOSTS (name, family_name, email, password, id, address, phone_number, city)
    VALUES (?,?,?,?,?,?,?,?)"""

    cursor.execute(text, (name, family, email, password, id, address, phone, city))
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
        post = turn_to_dict(cursor.fetchone())
        posts.append(post)
    return posts


def get_host_posts(host_id):
    text = """SELECT * FROM POSTS WHERE host_id=?"""
    cursor.execute(text, (host_id,))
    temp = cursor.fetchall()
    posts = []
    for item in temp:
        post = turn_to_dict(item)
        posts.append(post)
    return posts

def get_guest(email):
    text = f"SELECT * FROM GUESTS WHERE email=?"
    cursor.execute(text, (email,))
    item = cursor.fetchone()
    guest = turn_guest_to_dict(item)
    return guest

def get_host(email):
    text = f"SELECT * FROM GUESTS WHERE email=?"
    cursor.execute(text, (email,))
    item = cursor.fetchone()
    host = turn_host_to_dict(item)
    return host



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

def check_login(email, password):
    text = f"SELECT password FROM HOSTS WHERE email=?"
    cursor.execute(text, (email,))
    res = cursor.fetchone()
    if res is not None and res[0] == password:
        return True, consts.HOSTS
    text = f"SELECT password FROM GUESTS WHERE email=?"
    cursor.execute(text, (email,))
    res = cursor.fetchone()
    if res is not None and res[0] == password:
        return True, consts.GUESTS
    return False, False

def get_all_posts():
    text = f"SELECT * FROM POSTS"
    cursor.execute(text)
    temp = cursor.fetchall()
    posts = []
    for item in temp:
        post = turn_to_dict(item)
        posts.append(post)
    return posts

def turn_to_dict(item):
    return {"post_id": item[0],
            "host_id": item[1],
            "host_name": item[2],
            "host_family": item[3],
            "city": item[4],
            "address": item[5],
            "spots": item[6],
            "available": item[7],
            "content": item[8],
            "date" : item[9]}


def turn_guest_to_dict(item):
    print(item)
    return {"guest_id": item[0],
            "name": item[1],
            "family_name": item[2],
            "email": item[3],
            "password": item[4],
            }

def turn_host_to_dict(item):
    return {"host_id": item[0],
            "name": item[1],
            "family_name": item[2],
            "email": item[3],
            "password": item[4],
            "id": item[5],
            "address": item[6],
            "phone_number": item[7],
            "city" : item[8]
            }