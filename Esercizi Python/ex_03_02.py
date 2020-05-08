#Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. 
#If the score is between 0.0 and 1.0, print a grade using the following table:
#Score Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F
#If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85. 

#first we get the value of the score
score = input("Enter Score: ")

#now we try if the value is good, if it's not we get an error message and the program ends
try:
    sc = float(score)
except:
    print("Insert a valid score")
    quit()

#here by using if and elif statements we check the grade and we print the mark
if sc >= 0.9:
    print("A")
elif sc >= 0.8:
    print("B")
elif sc >= 0.7:
    print("C")
elif sc >= 0.6:
    print("D")
elif sc < 0.6:
    print("F")
