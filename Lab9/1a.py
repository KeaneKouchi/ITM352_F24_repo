# Write Python code that opens the file using the appropriate file mode 
# and displays the data type returned from open(). 
# Name: Keane Kouchi
# Date: 10/9/24


NamesText = open("names.txt", "r")

print(type(NamesText))

NamesText.close()