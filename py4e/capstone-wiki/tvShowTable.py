import sqlite3


conn = sqlite3.connect('capstoneWiki.sqlite')
cur = conn.cursor()

#DROP TABLE IF EXISTS Show;

cur.executescript('''
DROP TABLE IF EXISTS Show;

CREATE TABLE IF NOT EXISTS Show (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);
''')

fh = open("cleanList.txt", "r+")

for item in fh:
    show = item.strip()
    cur.execute('''INSERT OR IGNORE INTO Show (name)
        VALUES ( ? )''', ( show, ) )

conn.commit()

"""CREATE TABLE IF NOT EXISTS Language (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
)"""
