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
