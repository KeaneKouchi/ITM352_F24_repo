# Create a new tuple that includes the user input

# Name: Keane Kouchi
# Date: 9/27/24

ValuesTuple = ("hello", 10, "goodbye", 3, "goodnight", 5)

UserValues = input("Please enter a value: ")

try:
    #UserValues[-1] = UserValues
    ValuesTuple.append(UserValues)
except: 
    print("Error: You can't add elements to a tuple")

ValuesTuple = ValuesTuple + (UserValues,)

strings = 0

for values in ValuesTuple:
    if type(values) is str:
        strings += 1  

print(f"There are {strings} strings in the tuple.")