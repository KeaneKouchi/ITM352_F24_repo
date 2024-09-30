# Make a list of odd numbers between 1 and 50 using  
# list compression
# Name: Keane Kouchi
# Date: 9/27/24


OddNumbers = [number for number in range(1,51) if number % 2 != 0]

#alternative
#OddNumbers = [number for number in range(1,50,2)]

print("The odd numbers are: ",OddNumbers)