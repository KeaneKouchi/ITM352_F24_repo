# Ask the user to enter a sentence of their choosing.
# Caluculate the length of that string and return the value.
# Name: Keane Kouchi
# Date: 9/4/24

sentence = input("Please enter a sentence: ")

string_length = len(sentence)
string_length = str(string_length)
output_string = "You entered: \"" + sentence + "\". It has length: " + string_length
print(output_string)

