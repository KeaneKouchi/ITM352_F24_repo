# Using the .read() method, read the names from the names.txt file and 
# print out the names as well as a count of how many names there are altogether. 
# Name: Keane Kouchi
# Date: 10/9/24

with open('names.txt', 'r') as NamesText:

    print(type(NamesText))

    text = NamesText.read()

    print(text)

    #NamesList = text.splitlines()
    NamesList = text.split("\n")

    print(f"There are {len(NamesList)} names.")

    