import re

fname = input("Enter file name: ")
if len(fname) <1:
    fname = "Actual data.txt"
try:
    fh = open(fname)
except:
    print("File not found")
    quit()

total = list()

for line in fh:
    line = line.rstrip()
    stuff = re.findall('[0-9]+', line)
    if not stuff:
        continue
    for i in range(len(stuff)):
        stuff[i] = int(stuff[i])
        total.append(stuff[i])
print("Total sum: ", sum(total))
