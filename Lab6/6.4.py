# Determine a movie price. The rules are:
# The normal price is $14
# If someone is 65 or older, they pay $8.
# If it is Tuesday, the price is $10.
# If it is a matinee, the price is $5 for seniors and $8 otherwise
# Print out the values of the variables and the price. The price should always be the lowest one that applies.

# Name: Keane Kouchi
# Date: 9/25/24

NormalPrice = 14
SeniorPrice = 8
TuesdayPrice = 10
MatineeSeniorPrice = 5
MatineePrice = 8

Age = int(input("What is your age? "))
Matinee = input("Is it a matinee? ")
Day = input("Is is a tuesday? ")

#using method fropm 6.1a
Matinee = (False, True)[(Matinee.lower() == "yes")]
Day = (False, True)[(Day.lower() == "yes")]

#alternative with if/else
#if Matinee.lower() == "yes":
#    Matinee = True
#else: Matinee = False

#if Day.lower() == "yes":
#    Day = True
#else: Day = False

if Age >= 65 and Matinee == True:
    print(f"The price is ${MatineeSeniorPrice}")
elif Age >= 65 and Matinee == False:
    print(f"The price is ${SeniorPrice}")
elif Age < 65 and Matinee == True:
    print(f"The price is ${MatineePrice}")
elif Age < 65 and Matinee == False and Day is True:
    print(f"The price is ${TuesdayPrice}")
else: print(f"The price is ${NormalPrice}")
