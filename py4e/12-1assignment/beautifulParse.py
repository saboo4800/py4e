import urllib.request, urllib.parse, urllib.error, re
from bs4 import BeautifulSoup
import ssl

def gimmieSoup(link):
    #return parsable html
    html = urllib.request.urlopen(link, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
Total = 0
Count = 0
url = input('What url? ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
#print(soup)
tags = soup('span')
for tag in tags:
   val = int(tag.contents[0])
   Total += val
   Count += 1
print('Count',Count)
print('Sum',Total)

# Look at the parts of a tag
"""
print('TAG:',tag)
print('URL:',tag.get('href', None))
print('Contents:',tag.contents[0])
print('Attrs:',tag.attrs)
"""
