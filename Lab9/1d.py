# Rewrite 1c using the .readline() method.
# 
# Name: Keane Kouchi
# Date: 10/9/24

with open('names.txt', 'r') as NamesText:
    print(type(NamesText))

    NamesList = []
    
    while True:
        name = NamesText.readline()
        if not name:
            break
        NamesList.append(name.strip())

    for name in NamesList:
        print(name)

    print(f"There are {len(NamesList)} names.")