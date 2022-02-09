"""9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest
number of mail messages. The program looks for 'From ' lines and takes the second word of those lines
as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail
address to a count of the number of times they appear in the file. After the dictionary is produced,
the program reads through the dictionary using a maximum loop to find the most prolific committer."""
histogram = dict()
fname = input("Enter file name: ")
bigKey = None
bigVal = None
if len(fname) > 1:
    fhandle = open(fname)
else:
    fhandle = open('mbox-short.txt')
for line in fhandle:
    if line.startswith('From '):
        list = line.split()
        histogram[list[1]] = histogram.get(list[1],0)+1
#print(histogram.items())

for k,v in histogram.items():
    if bigVal == None:
        bigVal = v
        bigKey = k
    elif bigVal < v:
        bigVal = v
        bigKey = k

print(bigKey,histogram[bigKey])

"""
for v in histogram:
    if bigKey == None:
        bigKey = k
        bigVal = v
    elif bigVal < v:
        bigKey = k
        bigVal = v
"""
