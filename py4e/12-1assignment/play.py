import urllib.request, urllib.parse, urllib.error, re
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

word = input("what word do you want the definition to: ")
#make url with requested word
#html = urllib.request.urlopen('https://jisho.org/api/v1/search/words?keyword=' + word, context=ctx).read()
html = urllib.request.urlopen('https://jisho.org/search/' + word, context=ctx).read()



soup = BeautifulSoup(html, 'html.parser')
count=0
print(soup)
print("***000***000***")
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))

"""
for line in fhand:
    #print('reading')
    boop = line.decode().strip()
    print(boop)
    count +=1
    print(count)
    #print('stripped')
    #definition = re.findall('<span class="meaning-meaning">(.*?)<',boop)
    #if len(definition) > 0:
    #    break
#I feel so powerful
"""
