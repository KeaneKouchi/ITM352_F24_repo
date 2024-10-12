# Rewrite 1d using the .readlines() method.
# 
# Name: Keane Kouchi
# Date: 10/9/24

with open('names.txt', 'r') as NamesText:
    print(type(NamesText))

    NamesList = NamesText.readlines()
    
    NamesList = [name.strip() for name in NamesList]

    for name in NamesList:
        print(name)

    print(f"There are {len(NamesList)} names.")