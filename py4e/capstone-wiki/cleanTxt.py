import re

fh = open("showList.txt", 'r+')
start = None
end = None
fout = open("cleanList.txt", 'w+')
for item in fh:
    start = item.find("[")
    if item.rfind("|") > 0:
        end = item.rfind("|")
    else:
        end = item.rfind("]")-1
    edit = item[start+2:end]
    edit.strip()
    fout.write(edit+"\n")
