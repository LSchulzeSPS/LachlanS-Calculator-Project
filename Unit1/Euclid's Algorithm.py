yes = 'y'
while yes == 'y':
    print("preparing to find the GCD")
    n3 = int(input("Input a number: "))
    n2 = int(input("Input a second number: "))
    n1 = 1
    while n1 != 0:
        n1 = n3 % n2
        n3 = n2
        n2 = n1
    print(f"The GCD is {n3}")
    yes = input("Do you want to find another GCD (y/n): ").lower()
