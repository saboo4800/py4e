import urllib.request, urllib.parse, urllib.error, re
import ssl
import json
import time
import sys
import os
import pyperclip
#returns True if index is in a list
def index_in_list(a_list, index):
    if index + 1 < len(a_list):
        return True
    else:
        return False

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
#no idea what that does, pasted from https://stackoverflow.com/questions/14685999/trigger-an-event-when-clipboard-content-changes
sys.path.append(os.path.abspath("SO_site-packages"))

print("copy a word to your clipboard to begin")
word = pyperclip.paste()
while True:
    #watches clipboard for any changes and brings them in
    tmp_value = pyperclip.paste()
    if tmp_value != word:
        word = tmp_value
        print("Looking up: %s" % str(word)[:20])
    #Setting up to concatenate word to api endpoint url (at least I believe that's what it's called)
        words = dict()
        words['keyword'] = word
        print('making url')
        url = 'https://jisho.org/api/v1/search/words?' + urllib.parse.urlencode(words) #urlencode takes dictionary and formats enteries to be in url
        uh = urllib.request.urlopen(url)
        #getting and interpreting data
        data = uh.read().decode()
        try:
            js = json.loads(data)
        except:
            js = None
            #checks status of website, if not 'ok' goes back to word input
        if not js or "status" not in js["meta"] or js["meta"]["status"] != 200:
            print('==== Failure To Retrieve ====')
            print('==== Dumping Data ====')
            #print("===Pretty JSON===")
            print(json.dumps(js, indent=4, ensure_ascii=False))
            continue
        if index_in_list(js["data"],1):
            print("Retrieving word - IF")
            print("====Definition 1",js["data"][0]["japanese"],js["data"][0]["senses"][0]["english_definitions"])
            print("====Definition 2",js["data"][1]["japanese"],js["data"][1]["senses"][0]["english_definitions"])
            print(url)
            continue
        else:
            print("Retrieving word - ELSE")
            #print(json.dumps(js, indent=4, ensure_ascii=False))
            print("====Definition 1",js["data"][0]["japanese"],js["data"][0]["senses"][0]["english_definitions"])
            print(url)
            continue
    else:
        time.sleep(1.0)
        continue
    time.sleep(1.0)

#NEEDS TESTING - '死傷者'
