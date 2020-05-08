
#Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values 
#and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
# Use the file name mbox-short.txt as the file name

#first we get the name of the file
fname = input("Enter file name: ")

#now we check if the file exists with a try catch so that we don't get traceback errors
try:
    fh = open(fname)
except:
    print("File not found")
    quit()
    
#we initialize a total variable and a counter to 0
tot = 0
counter = 0

#with this loop we check if the lines in the file don't start with the string we need
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
     continue
    
    #here we slice to get only the line from the : on
    line = line [19:]
    
    #we delete left blankspaces with .lstrip()
    fline = float (line.lstrip())
    
    #we update the value of counter and total
    tot = tot + fline
    counter =  counter + 1
    
#we print the average dividing tot to counter 
print("Average spam confidence:", tot / counter)
