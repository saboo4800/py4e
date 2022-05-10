#!/usr/bin/python3

"""
    langlinks.py
    MediaWiki API Demos
    Demo of `Langlinks` module: Get a list of language links that a given page has
    MIT License

    S = requests.Session()

    URL = "https://en.wikipedia.org/w/api.php"

    PARAMS = {
        "action": "query",
        "titles": name,
        "prop": "langlinks",
        #"prop": "100",
        "format": "json"
    }



    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()

    print(json.dumps(DATA, indent=4, ensure_ascii=False))


    #print(DATA)

"""

import requests
import json
import sqlite3
import wikipediaapi

def print_langlinks(page):
    langlinks = page.langlinks
    for k in sorted(langlinks.keys()):
        #v = langlinks[k]
        print("%s" % (k))
    print(count)

#conn = sqlite3.connect('testWiki.sqlite')
#cur = conn.cursor()
name = input("What page do you want the languages of? ")

wiki = wikipediaapi.Wikipedia('en')
page = wiki.page(name)

print_langlinks(page)
