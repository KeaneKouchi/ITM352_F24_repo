# Rewrite the code to only open the file if it exists and is readable.
# 
# Name: Keane Kouchi
# Date: 10/9/24

try:
    with open('names.txt', 'r') as NamesText:
        print(type(NamesText))

        NamesList = NamesText.readlines()

        NamesList = [name.strip() for name in NamesList]

        for name in NamesList:
            print(name)

        print(f"There are {len(NamesList)} names.")
except FileNotFoundError:
    print("Invalid file name")