#Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
#Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours.
#Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation. 
#The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
#You should use input to read a string and float() to convert the string to a number. 
#Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly. 
#Do not name your variable sum or use the sum() function. 

#we start by defining the computepay function using def statement, we get hour and rate as arguments to the function
def computepay(h, r):
    #here we check if the hours are more than 40 and calculate the pay
    if(h < 40):
        return (h * r)
    else:
        return ((40 * r) + ((h - 40) * (r * 1.5)))

#here we get the input from the user
hours = input("Enter Hours: ")

#here we test if the input is good
try:
    hrs = float(hours)
except:
    print('invalid input')
    quit()

#we do the same things as hour for the ratePerHour
ratePerHour = input('Enter Rate Per Hour: ')
try:
    rate = float(ratePerHour)
except:
    print("Invalid input")
    quit()

#now we use our function to compute the pay passing as arguments hrs and rate
p = computepay(hrs, rate)
print("Pay", p)
