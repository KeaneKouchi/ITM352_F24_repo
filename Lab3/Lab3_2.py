# Ask the user to enter two numbers and return the midpoint
# 
# Name: Keane Kouchi
# Date: 9/11/24

def midpoint(num1, num2):
    return ((num1 + num2)/2)

number1 = float(input("Enter first value:"))
number2 = float(input("Enter second value:"))

mid = midpoint(number1, number2)
print("The midpoint is:", mid)
