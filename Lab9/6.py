# Write a program to read the JSON file that you created in question 5 and print it. 
# You may put this into your Assignment 1 if you wish.

# Name: Keane Kouchi
# Date: 10/9/24

import json

with open('questions.json', 'r') as file:
    QUESTIONS = json.load(file)
    print(type(QUESTIONS))
    print(QUESTIONS)