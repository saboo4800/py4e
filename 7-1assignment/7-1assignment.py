# Use words.txt as the file name

try:
    fname = input("Enter file name: ")
except:
    print('invalid file name')
    quit()
fh = open(fname)
inp = fh.read()
count = 0
for line in inp:
    line.rstrip()
    count += 1
print(inp.upper())
print(count)
