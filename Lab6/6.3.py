# 3.  A leap year is a year that consists of 366 (not 365) days. It occurs roughly every four years. 
# More specifically, a year is considered leap if it is either divisible by 4 but not by 100 or it is divisible by 400.
# Write a program that asks the user for a year and replies with either "leap year" or "not a leap year".

# Name: Keane Kouchi
# Date: 9/25/24

Year = int(input("Please enter a year:"))

if (Year % 4 == 0 and Year % 100 != 0) or (Year % 400 == 0):
    print(Year, "is a leap year")

else: print(Year, "is not a leap year")

