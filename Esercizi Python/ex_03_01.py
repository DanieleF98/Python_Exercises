#Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
#Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. 
#Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
#You should use input to read a string and float() to convert the string to a number. 
#Do not worry about error checking the user input - assume the user types numbers properly. 

#we get hours and ratePerHour from tha user
hours = input('Enter Hours:')
ratePerHour = input('Enter Rate For Hour:')

#we convert it into float type using the float() function
h = float(hours)
r = float(ratePerHour)

#now with this if statement we check if the hours are more or less than 40
if h < 40:
	#if we have less than 40 hours we just need to multiply hours and ratePer Hours 
	print(h * r)
else:
	#if we have more than 40 hours we multiply 40 hours for the ratePerHour to get the hours we get payd normally
	standardHour = 40 * r
	#than we get the extraHour bu subtracting the normal 40 hours and increasing ratePerHour by 1.5 times
	extraHour = (h - 40) * (r* 1.5)
	print(standardHour + extraHour)

#we could have done this more easily just putting everything inside the print statement
	#print((40 * r) + ((h - 40) * (r * 1.5)))

#if we wanted to check if the input were good we could have done
#try:
	#h = float(hours)
#except:
	#print('invalid input')
	#quit()
