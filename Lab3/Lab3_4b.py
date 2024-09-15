# Ask the user to enter two numbers and return the value
# of the larger one
# Name: Keane Kouchi
# Date: 9/11/24

from HandyMath import max

#def max(num1,num2):
#    return (num1 > num2)* num1 + (num2 >= num1) * num2


number1 = float(input("Enter a number:"))
number2 = float(input("Enter a second number:"))


maximum = max(number1,number2)
print("The larger number is:", maximum)