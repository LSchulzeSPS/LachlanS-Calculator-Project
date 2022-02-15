#Create a function that takes 2 numbers and MULTIPLIES them together, returning the result
#Create a function that takes 2 numbers and DIVIDE them together, returning the result
#Create a function that takes 2 numbers and ADDS them together, returning the result
#Create a function that takes 2 numbers and SUBTRACTS them together, returning the resul
go = 'y'
def Add(n1, n2): print(f"{n1} + {n2} = {n1+n2}")
def Subtract(n1, n2): print(f"{n1} - {n2} = {n1-n2}")
def Multiply(n1, n2): print(f"{n1} x {n2} = {n1*n2}")
def Divide(n1, n2): print(f"{n1} ÷ {n2} = {n1/n2}")
while go == 'y':
    asmd = int(input("Do you want to add(1), subtract(2), multiply(3) or divide(4): "))
    if asmd == 1: Add(n1 = int(input("Input your first number to be added: ")), n2 = int(input("Input your second number to be added to your first: ")))
    elif asmd == 2: Subtract(n1 = int(input("Input your first number that will be subtracted by your second number: ")), n2 = int(input("Input your second number subtract your first: ")))
    elif asmd == 3: Multiply(n1 = int(input("Input your first number to be multiplied together: ")), n2 = int(input("Input your second number multiplied together: ")))
    elif asmd == 4: Divide(n1 = int(input("Input your first number that will be divided by your second: ")), n2 = int(input("Input your second number that will divide your first number: ")))
    go = input("Do you want to use this calculator again?(y/n): ")
print("Thankyou for using this premium calculator")
