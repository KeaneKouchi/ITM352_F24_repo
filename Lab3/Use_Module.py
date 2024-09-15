# Program to test the use of math functions library

import HandyMath as HM


number1 = float(input("Enter first value:"))
number2 = float(input("Enter second value:"))

#midpoint test
mid = HM.midpoint(number1, number2)
print(f"The midpoint of {number1} and {number2} is: {mid}")


#squareroot test
number1 = float(input("Enter a number:"))

SR = HM.squareroot(number1)
print(f"The squareroot of {number1} is: {SR}")


#exponentiation test
number = input("Enter a whole base number:")
exponent = input("Please enter a number to be used as the exponent:")

number=float(number)
exponent=float(exponent)

EXP = HM.exponentiation(number,exponent)
print(f"{number} raised to the {exponent} power is: {EXP}")


#max test
number1 = float(input("Enter a number:"))
number2 = float(input("Enter a second number:"))

maximum = HM.max(number1,number2)
print(f"The larger number of {number1} and {number2} is: {maximum}")


#min test
number1 = float(input("Enter a number:"))
number2 = float(input("Enter a second number:"))

minimum = HM.min(number1,number2)
print(f"The smaller number of {number1} and {number2} is: {minimum}")