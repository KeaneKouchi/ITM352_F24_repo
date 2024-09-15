# Library of math functions

#function to find a midpoint
def midpoint(num1, num2):
    return ((num1 + num2)/2)


#function to find the squareroot
def squareroot(number):
    return (number**0.5)


#exponentiation function
def exponentiation(number,exponent):
    return ((number**exponent))


#max function
def max(num1,num2):
    return (num1 > num2)* num1 + (num2 >= num1) * num2


#min function
def min(num1,num2):
    return (num1 < num2)* num1 + (num2 <= num1) * num2

