# Program to count letter frequencies in a string
#
# Keane Kouchi
# 9/27/2024

def GetFrequencies(String):
    FreqDict = {}
    for character in String:
        character = character.lower()
        if character not in FreqDict: FreqDict[character] = 1
        else: FreqDict[character] += 1
    return FreqDict



UserInput = input("Please enter a string: ")

dict = GetFrequencies(UserInput)
print(dict)