name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
try:
    fh= open(name)
except:
    print("File not found")
    quit()
counts = dict()
for line in fh:
    if not line.startswith('From '):
        continue
    word = line.split()
    sline = word[5]
    counts[sline[:2]] = counts.get(sline[:2],0)+1

lst = list()
for key,val in counts.items():
    newtup = (key,val)
    lst.append(newtup)
lst = sorted(lst)
for key,val in lst:
    print(key,val)
