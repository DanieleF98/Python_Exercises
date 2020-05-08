counter = 0
sum = 0
while True:
    num = input("Enter a number: ")
    if num == 'done':
        break
    try:
        Inum = int (num)
    except:
        print("Invalid imput")
        continue
    counter = counter + 1
    sum = sum + Inum
print(sum, counter, sum / counter)
