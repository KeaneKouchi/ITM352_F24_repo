# Make a list of odd numbers between 1 and 50 using range and an if statement
# 
# Name: Keane Kouchi
# Date: 9/27/24

OddNumbers = []

for numbers in range(1,50):
    if numbers % 2 != 0:
        OddNumbers.append(numbers)

print("The odd numbers are: ",OddNumbers)