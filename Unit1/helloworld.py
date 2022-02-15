#CTRL + / multi line comment

# print("Hello, World!")
# name = "Lachlan"
# print("My name is", name + ".")  #using variables in a string
# teacher = "Mr Fenwick"
# print(f"My teacher is {teacher}.")  #using an f string

# print("# Square List - multi line version")
# squares = []
# for i in range(10):
#     squares.append(i**2)
# print(squares)
#
# print("#squares - one line version")
# print([i**2 for i in range(10)])

# print(10 % 4)   #remainder

# for i in range(3):
#     print("' '' '''")

# print(5**2)
# print(9 * 5)
# print(15 / 12)
# print(12 / 15)
# print(15 // 12)
# print(12 // 15)
# print(5 % 2)
# print(9 % 5)
# print(15 % 12)
# print(12 % 15)
# print(6 % 6)
# print(0 % 7)

# # Take the number 1000 and make it number
# n = int(input("Please input a number to have their prime factors evaluated: "))
# nf = n
# prime_factors = []
# uf = True
# # Divide number by 2, if it is a whole number make that number the new number and put 2 as a prime factor, repeat step 2
# while uf == True:
#     if n % 2 == 0:
#         n = n / 2
#         prime_factors.append(", 2")
# # Divide number by 3, if it is a whole number make that number the new number and put 3 as a prime factor, repeat step 2
#     elif n % 3 == 0:
#         n = n / 3
#         prime_factors.append(", 3")
# # Divide number by 5, if it is a whole number make that number the new number and put 5 as a prime factor, repeat step 2
#     elif n % 5 == 0:
#         n = n / 5
#         prime_factors.append(", 5")
# # If neither step 2, 3 or 4 works, write down number as a prime factor
#     else:
#         uf = False
#         prime_factors.append(str(n))
#         print(f"The prime numbers of {nf} are{' '.join(prime_factors)}")

# numbers = []
# n = 0
# Problem = input("Please insert an addition problem: ")
# for i in Problem:
#     numbers.append(i)
# for characters in numbers:
#     if characters == '1234567890':
#         n = n + int(characters)
# print(n)






