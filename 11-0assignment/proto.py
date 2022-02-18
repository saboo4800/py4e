#Make a dictionary of all words in a doc. print 10 most frequent words

while True:
    try:
        fname = input("Input file name: ")
        fhand = open(fname)
        break
    except:
        print('Invalid filename')
        continue
topNum = int(input("How many results do you want to see? "))
bank = dict()
tup = []
index = 0
for line in fhand:
    line.rstrip()
    words = line.split()
    for word in words:
        #word.lower()
        #word.rstrip()
        #word.lstrip()
        bank[word] = bank.get(word,0) + 1
        #tup.append((bank[word],word))
        #print(bank[word],word)

for key,val in bank.items():
    tup.append((val,key))
tup.sort(reverse=True)

while topNum > 0:
    print (tup[index])
    index +=1
    topNum -=1
