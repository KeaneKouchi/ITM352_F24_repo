# Ask the user to enter two numbers and return the value
# 
# Name: Keane Kouchi
# Date: 9/11/24

def exponentiation(number,exponent):
    return ((number**exponent))

number = float(input("Enter a whole base number:"))
exponent = float(input("Please enter a number to be used as the exponent:"))

#number=float(number)
#exponent=float(exponent)

EXP = exponentiation(number,exponent)
print("The answer is:", EXP)