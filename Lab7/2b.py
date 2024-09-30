# Re-write 2a using a condition checking the last element on the list is 
# less than or equal to 50 
# Name: Keane Kouchi
# Date: 9/27/24


EvenNumbers =[]

Number = 2

while Number <= 50:
    if len(EvenNumbers) == 0 or EvenNumbers[-1] <= 50:
        EvenNumbers.append(Number)
    Number += 2

print("The even numbers are: ",EvenNumbers)