#!/usr/bin/python3

"""
    langlinks.py
    MediaWiki API Demos
    Demo of `Langlinks` module: Get a list of language links that a given page has
    MIT License
"""

import requests
import json

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "titles": "Mister Rogers' Neighborhood",
    #"prop": "langlinks",
    "prop": "100",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(json.dumps(DATA, indent=4, ensure_ascii=False))


#print(DATA)
