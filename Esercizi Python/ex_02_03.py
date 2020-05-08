'''Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25). 
You should use input to read a string and float() to convert the string to a number. 
Do not worry about error checking or bad user data.'''

#gets hours and ratePerHour from keyboard input
hours = input('How many hours : ')
ratePerHour = input('What is the rate per hour?')
#converts hours and ratePerHour into float type so that we can use them as number
fhours = float(hours)
fratePerHour = float(ratePerHour)
#prints the pay multiplying the value of hours and the ratePerHour
print('Pay :', (hours * ratePerHour)
#we could have done this in only one step and convert the values directly into the print statement:
#print('Pay :', (float(hours) * float(ratePerHour)))
'''if we wanted to check the user data to exclude bad data, we could have used the try except
try:
    fhours = float(hours)
except:
    print('invalid data input')
    quit() '''
