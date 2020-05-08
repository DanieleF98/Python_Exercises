fname = input('Enter file name: ')
try:
    fh = open(fname)
except:
    print('File not found')
    quit()

counts = dict()
for line in fh:
    line = line.strip()
    if not line.startswith("From "):
        continue
    word = line.split()
    sline = word[1]
    counts[sline] = counts.get(sline,0)+1

bigCount = None
bigMail = None
for word,count in counts.items():
    if bigCount is None or count > bigCount:
        bigWord = word
        bigCount = count
print(bigWord,bigCount)
