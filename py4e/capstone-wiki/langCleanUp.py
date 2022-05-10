import re

fh = open("cleanList3.txt","r+")
#fout = open("cleanList4.txt", 'w+')
ids = list()
count = 0
langList = list()
langCode = list()
container = dict()
store = fh.readlines()

for item in store:
    langList = re.findall("\[\[(\w*.\w*\s*\w*)\|*",item)
    primary = langList[0]
    if primary.find("]") >-1:
        primary = primary[:primary.find("]")]
    elif primary.find("|") >-1:
        primary = primary[:primary.find("|")]

    langCode = re.findall("id=\"([a-z]+)\"",item)

    container[langCode[0]] = primary
    count +=1
for k, v in container.items():
    #fout.writelines(k+" "+v+"\n")
    print(k,v)

fh.close()
fout.close()

'''
for item in store:
    if item.find("|-") != 0:
        print(item)
        print("\/\/\/\/\/\/\/")
        fout.write(item)

for item in store:
    end = item.find("||")
    fout.write(item[:end] + "\n")
'''
