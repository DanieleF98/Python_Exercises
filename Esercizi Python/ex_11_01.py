#In this assignment you will read through and parse a file with text and numbers. 
#You will extract all the numbers in the file and compute the sum of the numbers. 

#we import the library for regular expressions
import re

#we ask the user for the name of the file
fname = input('Enter file name: ')

#if we only hit enter we'll automatically get the name of the file that we want
if len(fname) <1:
    fname = 'Actual data.txt'

#we check if the file exists and if it doesn't we print an error message and close the program
try:
    fh = open(fname)
except:
    print('File not found')
    quit()

#we declare an empty list
total = list()

#with this cicle we want to get all the numbers from the file, convert them to int and store them inside the total list
for line in fh:
    line = line.rstrip()
    
    #the result of this line of code is to get all the numbers contained in each line as a list of strings inside numList
    numList = re.findall('[0-9]+', line)
    
    #if there are no numbers in the line we'll get an empty line, which is going to be true to the if not statement
    if not numList:
        continue
        
    #here we convert every values inside the list to int and we put them inside the total list 
    for i in range(len(numList)):
        numList[i] = int(numList[i])
        total.append(numList[i])

#we print the total sum of the numbers in the total list
print("Total sum: ", sum(total))
