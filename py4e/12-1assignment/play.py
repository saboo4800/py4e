import urllib.request, urllib.parse, urllib.error, re
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def gimmieSoup(word):
    #return parsable html
    html = urllib.request.urlopen('https://jisho.org/search/' + word, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup

word = input("what word do you want the definition to: ")
#make url with requested word
#html = urllib.request.urlopen('https://jisho.org/api/v1/search/words?keyword=' + word, context=ctx).read()
#html = urllib.request.urlopen('https://jisho.org/search/' + word, context=ctx).read()

soup = gimmieSoup(word)
count=0
#print(soup)
#print("***000***000***")
#tags = soup('a')
#tags = soup('span')
#print(soup.prettify())

for tag in soup.find_all(re.compile("^b")):
    print(tag.name)

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
