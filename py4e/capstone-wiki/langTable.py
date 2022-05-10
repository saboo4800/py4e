import sqlite3

conn = sqlite3.connect('capstoneWiki.sqlite')
cur = conn.cursor()

fh = open("cleanListFinal.txt","r+")

cur.executescript('''
DROP TABLE IF EXISTS Language;

CREATE TABLE IF NOT EXISTS Language (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    code    TEXT UNIQUE,
    lang    TEXT UNIQUE
);
''')

for item in fh:
    code = item[:2]
    code = code.strip()
    lang = item[3:]
    lang = lang.strip()
    print(code)
    print(lang)
    cur.execute('''INSERT OR IGNORE INTO Language (code,lang)
        VALUES ( ?,? )''', ( code,lang ) )

conn.commit()
