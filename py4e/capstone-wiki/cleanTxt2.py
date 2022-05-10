import re

fh = open("cleanList.txt", 'r+')
start = None
end = None
fout = open("cleanList2.txt", 'w+')
for item in fh:
    item.strip()
    end = len(item)
    if item.startswith("''"):
        item = item[2:]
    if re.search("'\n",item) != None:
        item = re.sub("'","",item)
    if re.search("#",item) != None:
        item = item[:item.index("#")]
    fout.write(item)
