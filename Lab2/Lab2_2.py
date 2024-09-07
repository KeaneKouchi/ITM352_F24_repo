# Ask the use to enter their birth year as a 4 digit number
# Calculate their age and return the value
# Name: Keane Kouchi
# Date: 9/4/24

birth_year = input("Please enter your year of birth as a 4 digit number: ")

birth_year = int(birth_year)
# This should be changed, should not hard-code the year.
current_year = 2024
#This doesn't take into account the month. Need to fix.
age = (current_year-birth_year)
print("You entered: ",birth_year)
print("Your age is =",age)
