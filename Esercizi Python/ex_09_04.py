
#Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
#The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
#The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they 
#appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop 
#to find the most prolific committer.

#we start by getting the name of the file from input
fname = input('Enter file name: ')

#with this if i can just press enter and the program will automatically set the name to the value of mbox.short.txt
if len(fname) < 1 :
    fname = 'mbox-short.txt'
    
#we check if the file exists
try:
    fh = open(fname)
except:
    print('File not found')
    quit()

#we create a dictionary
counts = dict()

#with this loop we get all the emails and we count how many times they appear
for line in fh:
    
    #we eliminate left spaces
    line = line.strip()word
    
    #we check if the lines starts with From 
    if not line.startswith('From '):
        continue
        
    #we divide the line into words contained in a list of strings
    word = line.split()
    
    #we get the email, which is the second word
    sline = word[1]
    
    #we count the occurrences of the mail inside the dictionary, if it's the first time we see them we'll set value of 1
    counts[sline] = counts.get(sline,0)+1

#we set two variables for bigger key and bigger value of the dictionary
bigCount = None
bigMail = None

#we make a loop with two iteration variable to search inside the tuples generated by the method .items()
for word,count in counts.items():
    
    #basic code to calculate max and put it inside variables
    if bigCount is None or count > bigCount:
        bigWord = word
        bigCount = count
print(bigWord,bigCount)
