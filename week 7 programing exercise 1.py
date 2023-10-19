n = int(input("Enter how many numbers: "))
num1 = 0
num2 = 0
numtotal = 1

for i in range(n):
    num1 = num2
    num2 = numtotal
    numtotal = num1 + num2
    print(numtotal)

