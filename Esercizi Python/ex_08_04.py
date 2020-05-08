
#Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method.
#The program should build a list of words. For each word on each line check to see if the word is already in the list 
#and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order. 

#we get input from the user
fname = input("Enter file name: ")

#we check if the file exists
try:
    fh = open(fname)
except:
    print('file not found')
    quit()
    
#we create an empty lists so that we can put objects in it later
lst = list()

#with the for loop we go through all the file line by line
for line in fh:
    #we split the line in words with the .split() method
    wline = line.split()
    
    #we go through each word in wline
    for word in wline:
        
        #if the word is not in the list we put it at the end of the list with the .append() method
        if word not in lst:
            lst.append(word)

#here we sort the list and print it
lst.sort()
print(lst)
