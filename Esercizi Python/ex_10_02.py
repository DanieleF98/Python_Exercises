#Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day 
#for each of the messages. You can pull the hour out from the 'From ' line by finding the time 
#and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

#we get the name of the file
name = input("Enter file:")

#we check if the file exists
if len(name) < 1 : name = "mbox-short.txt"
try:
    fh= open(name)
except:
    print("File not found")
    quit()
    
#we create a dictionary
counts = dict()

#with this code we search the hour and put it inside the dictionary
for line in fh:
    
    #we check if the file starts with "From "
    if not line.startswith('From '):
        continue
    
    #we split the line in words and get the hours inside the dictionary counting the occurrences
    word = line.split()
    sline = word[5]
    counts[sline[:2]] = counts.get(sline[:2],0)+1

#we create a list
lst = list()

#with this loop we get the tuples inside the list 
for key,val in counts.items():
    newtup = (key,val)
    lst.append(newtup)

#we sort the tuples inside the list from smallest to biggest using the sorted function
lst = sorted(lst)

#we print the tuples we just ordered 
for key,val in lst:
    print(key,val)
