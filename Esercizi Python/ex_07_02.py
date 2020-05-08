# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("File not found")
    quit()
tot = 0
counter = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
     continue
    line = line [19:]
    fline = float (line.lstrip())
    tot = tot + fline
    counter =  counter + 1
print("Average spam confidence:", tot / counter)
