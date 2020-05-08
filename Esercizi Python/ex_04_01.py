def computepay(h, r):
    if(h < 40):
        return (h * r)
    else:
        return ((40 * r) + ((h - 40) * (r * 1.5)))

hours = input("Enter Hours: ")
try:
    hrs = float(hours)
except:
    print("Insert a number")
ratePerHour = input("Enter Rate Per Hour: ")
try:
    rate = float(ratePerHour)
except:
    print("Insert a number")
p = computepay(hrs, rate)
print("Pay", p)
