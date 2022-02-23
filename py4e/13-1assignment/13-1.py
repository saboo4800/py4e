import urllib.request, urllib.parse, urllib.error, re
import ssl
import xml.etree.ElementTree as ET

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter location: ")

stuff = urllib.request.urlopen(url, context=ctx)
print('Retrieving',url)

data = stuff.read()
print("retrieved",len(data),"characteres")

tree = ET.fromstring(data)

counts = tree.findall('.//count')
print("Count:",len(counts))
total = 0
for num in range(len(counts)):
    digit = counts[num].text
    digit = int(digit)
    total += digit
print("Sum:",total)
