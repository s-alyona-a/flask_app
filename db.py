'''import sqlite3

db = sqlite3.connect('servey.db')
cur = db.cursor()
cur.execute(
    """CREATE TABLE answers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    q1 INTEGER,
    q2 INTEGER,
    q3 INTEGER,
    q4 INTEGER,
    q5 INTEGER,
    q6 INTEGER,
    q7 INTEGER,
    q8 INTEGER,
    q9 INTEGER,
    q10 INTEGER)
    """)

cur.execute(
    """CREATE TABLE questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT
    )""")

cur.execute(
    """CREATE TABLE 
    user ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    age INTEGER, 
    gender TEXT,
    education TEXT,
    linguistics TEXT)""")

db.commit()
with app.app_context():
    db.create_all()

data = [(1, 'Я случайно упал со стула'), (2, 'Я нечаянно упал со стула'),
        (3, 'Ваза случайно разбилась'), (4, 'Ваза нечаянно разбилась'),
        (5, 'Мы случайно встретились'), (6, 'Мы нечаянно встретились'),
        (7, 'Он позвонил не случайно'), (8, 'Он позвонил не нечаянно'),
        (9, 'Петя случайно попал в хор'), (10, 'Петя нечаянно попал в хор')]
cur.executemany(
    """INSERT INTO questions (id, text) values (?, ?)""", data)
db.commit()'''