import re
fname = 'regex_sum_1429178.txt'
fhand = open(fname)
lst = []
actualSum = 445833
for line in fhand:
    x = re.findall('[0-9]+',line)
    if len(x) > 0:
        for item in x:
            item = int(item)
            lst.append(item)
sum = sum(lst)
print(sum)
