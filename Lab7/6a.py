# try to append to a tuple

# Name: Keane Kouchi
# Date: 9/27/24

ValuesTuple = ("hello", 10, "goodbye", 3, "goodnight", 5)

UserValues = input("Please enter a value: ")

ValuesTuple.append(UserValues) 

strings = 0

for values in ValuesTuple:
    if type(values) is str:
        strings += 1  

print(f"There are {strings} strings in the tuple.")