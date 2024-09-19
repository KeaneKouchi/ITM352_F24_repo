# Ask the user to enter their first name, middle initial, and last name
# Concatenate them together with spaces in between and print
# Name: Keane Kouchi
# Date: 9/18/24


FirstName = input("Please enter your first name:")
MiddleInitial = input("Please enter your middle initial:")
LastName = input("Please enter your last name:")

# +concatenation
#FullName = FirstName + " " + MiddleInitial + " " + LastName

# f string
#FullName = (f"{FirstName} {MiddleInitial} {LastName}")

# %operator
#FullName = "%s %s %s" % (FirstName, MiddleInitial, LastName)

# Format()
#FullName = "{} {} {}".format(FirstName, MiddleInitial, LastName)

# Join()
#NameList = [FirstName, MiddleInitial, LastName]
#FullName = " ".join(NameList)

# format() but unpack the list as the argument
NameList = [FirstName, MiddleInitial, LastName]
FullName = "{} {} {}".format(*NameList)

print("Your name is: ", FullName)