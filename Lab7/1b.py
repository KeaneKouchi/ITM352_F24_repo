# Make a list of odd numbers between 1 and 50 using range and 
# and the fact an odd number is 2*num + 1
# Name: Keane Kouchi
# Date: 9/27/24

OddNumbers = []

for number in range(0,25):
    OddNumber = 2 * number + 1
    OddNumbers.append(OddNumber)

print("The odd numbers are: ",OddNumbers)
