# Write Python code that uses the Python while statement to 
# create a list of elements that are even numbers from 1 to 50. 
# Name: Keane Kouchi
# Date: 9/27/24


EvenNumbers =[]

Number = 1

while Number <= 50:
    if Number % 2 == 0:
        EvenNumbers.append(Number)
    Number += 1

print("The even numbers are: ",EvenNumbers)