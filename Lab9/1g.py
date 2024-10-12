# Now add the name “Port, Dan” to the end of the file and 
# print the entire contents of the file. 
# Name: Keane Kouchi
# Date: 10/9/24

try:
    with open('names.txt', 'a') as NamesText:
        NamesText.write("\nPort, Dan")

    with open('names.txt', 'r') as NamesText:

        print(type(NamesText))

        NamesList = NamesText.readlines()

        NamesList = [name.strip() for name in NamesList]

        for name in NamesList:
            print(name)

        print(f"There are {len(NamesList)} names.")

except FileNotFoundError:
    print("Invalid file name")