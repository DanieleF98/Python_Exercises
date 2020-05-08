#Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
#Once 'done' is entered, print out the largest and smallest of the numbers. 
#If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. 
#Enter 7, 2, bob, 10, and 4 and match the output below. 

#we start by setting largest and smallest to None, we use it as a flag value
largest = None
smallest = None

#now we do a while loop to get data until the user writes 'done' 
while True:
    #here we get the value that the user inputs
    num = input("Enter a number: ")
    
    #now we check if num is equal to 'done', if it is we break out from the loop
    if num == 'done':
        break
        
    #we do a try except to see if the value we got from the user was good or not, if it's not we use the continue statement to go to the next iteration of the loop
    try:
        inum = int(num)
    except:
        print("Invalid input")
        continue
        
    #with this if we see if largest has value of None, and if it's None we put the first number inside it
    if largest is None:
        largest = inum
    #if the largest is not None we check and see if the number we got is larger or not than the largest, if it's largest we change the value of largest and put the number we got in it
    elif inum > largest:
        largest = inum
        
    #we do the same things as largest, but we want the lowest numbers
    if smallest is None:
        smallest = inum
    elif smallest > inum:
        smallest = inum
        
print("Maximum is", largest)
print("Minimum is", smallest)
