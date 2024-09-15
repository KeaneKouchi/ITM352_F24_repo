# Ask the user to enter two numbers and returns the value
# of the smaller one
# Name: Keane Kouchi
# Date: 9/11/24

def min(num1,num2):
    return (num1 < num2)* num1 + (num2 <= num1) * num2


number1 = float(input("Enter a number:"))
number2 = float(input("Enter a second number:"))


minimum = min(number1,number2)
print("The smaller number is:", minimum)