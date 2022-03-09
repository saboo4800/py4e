import urllib.request, urllib.parse, urllib.error, re
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count = 0
total = 0

while True:
    url = input("Enter URL: ")

    if len(url) < 1:
        break

    print('Retrieving',url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    print('Retrieved', len(data), "characters.")

    try:
        js = json.loads(data)
    except:
        js = None

    for item in js['comments']:
        num = int(item["count"])
        count +=1
        total += num
    print("count:",count)
    print("sum:",total)

'''
if not js or 'status' not in js or js['status'] != 'OK':
    print('====FAILURE TO RETRIEVE====')
    print(data)
'''
#print(json.dumps(js, indent=4))
