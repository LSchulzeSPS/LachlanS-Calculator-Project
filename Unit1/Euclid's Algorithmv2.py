yes = 'y'
def Euclid(n3, n2):
    n1 = 1
    while n1 != 0:
        n1 = n3 % n2
        n3 = n2
        n2 = n1
    print(f"The GCD is {n3}")

while yes == 'y':
    print("preparing to find the GCD")
    Euclid(n3 = int(input("Input a number: ")), n2 = int(input("Input a second number: ")))
    yes = input("Do you want to find another GCD (y/n): ").lower()
