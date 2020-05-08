fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    wline = line.split()
    for word in wline:
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst)
