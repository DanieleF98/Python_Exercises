#Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#You will parse the From line using split() and print out the second word in the line 
#(i.e. the entire address of the person who sent the message). Then print out a count at the end. 

#we get the file name
fname = input("Enter file name: ")

#we check if the file exists
try:
    fh = open(fname)
except:
    print('file not found')
    quit()
    
#we set a counter to 0
count = 0

#we go through each line in the file
for line in fh:
    
    #we split the line in words
    line = line.strip()
    
    #we check if the line does not starts with From 
    if not line.startswith("From "):
        continue
        
    #if the line .startswith(From) we split the line, update the counter and print the second word
    sline = line.split()
    count = count + 1
    print(sline[1])
print("There were", count, "lines in the file with From as the first word")
