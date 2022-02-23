import urllib.request, urllib.parse, urllib.error, re
from bs4 import BeautifulSoup
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def gimmieSoup(link):
    html = urllib.request.urlopen(link, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup

url = input('Enter url: ')
pos = int(input('Enter position: '))
count = int(input('Enter count: '))+1
tags = []

while count > 0:
    print("Retrieving:",url)
    tags = gimmieSoup(url)(('a'))
    url = tags[pos-1].get('href', None)
    count -= 1
"""
for tag in tags:
   val = int(tag.contents[0])
   Total += val
   Count += 1
print('Count',Count)
print('Sum',Total)
"""
#print(tags[2])

# Look at the parts of a tag
"""
for tag in tags:
    print('TAG:',tag)
    print('URL:',tag.get('href', None))
    print('Contents:',tag.contents[0])
    print('Attrs:',tag.attrs)
"""
