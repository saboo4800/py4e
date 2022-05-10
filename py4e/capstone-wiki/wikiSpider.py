import sqlite3
import wikipediaapi

fh = open("cleanList.txt")

def return_langlinks(page):
    langlinks = page.langlinks
    #for k in sorted(langlinks.keys()):
    #    print("%s" % (k))
    return sorted(langlinks.keys())

conn = sqlite3.connect('capstoneWiki.sqlite')
cur = conn.cursor()

cur.executescript('''
CREATE TABLE IF NOT EXISTS show_Language (
    show_id     INTEGER,
    language_id INTEGER,
    PRIMARY KEY (show_id,language_id))
''')

wiki = wikipediaapi.Wikipedia('en')

cur.execute('SELECT max(show_id) FROM show_Language' )
row = cur.fetchone()[0]-2

print(row)

fail = 0

while True:
    row +=1
    conn.commit()
    try:
        cur.execute('SELECT name FROM Show where id = ? ', (row,))
        show = cur.fetchone()[0]
    except:
        print("row not found")
        fail +=1
        if fail > 100:
            break
        continue
    page = wiki.page(show)
    if page.exists():
        print(show)
        langs = return_langlinks(page)
        langs.append('en')
        if langs:
            cur.execute('SELECT id FROM Show WHERE name = ? ', (show, ))
            show_id = cur.fetchone()[0]
            print(show_id)
            for code in langs:
                try:
                    print(code)
                    cur.execute('SELECT id FROM Language WHERE code = ? ', (code, ))
                    language_id = cur.fetchone()[0]
                    print(language_id,code)

                    cur.execute('''INSERT OR IGNORE INTO show_Language
                        (show_id, language_id) VALUES ( ?, ? )''',
                        ( show_id, language_id) )
                except Exception as e:
                    print("Lang ID missing from DB")
                    continue
        else:
            print('Only English Language Page Available')
            continue
    else:
        print("couldn't find:",show)
        continue

cur.close()
"""
start = None
cur.execute('SELECT max(id) FROM Messages' )
try:
    row = cur.fetchone()
    if row is None :
        start = 0
    else:
        start = row[0]
except:
    start = 0

if start is None : start = 0
"""
