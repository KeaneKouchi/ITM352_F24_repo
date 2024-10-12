# Write a program that takes the dictionary of quiz questions 
# you created for Assignment 1 and saves it as a JSON file. 
#
# Name: Keane Kouchi
# Date: 10/9/24

import json

QUESTIONS = {
    "What is the airspeed of an unladen swallow in miles per hour?": [
        "12",
        "8",
        "11",
        "15"
    ],
    "What is the capital of Texas?": [
        "Austin",
        "San Antonio",
        "Dallas",
        "Waco"
    ],
    "The Last Supper was painted by which artist?": [
        "Da Vinci",
        "Rembrandt",
        "Picasso",
        "Michelangelo"
    ],
    "Which classic novel opens with the line 'Call Me Ishmael'?": [
        "Moby Dick",
        "Wuthering Heights",
        "The Old Man and the Sea",
        "The Scarlet Letter"
    ],
    "Frank Lloyd Wright designed a house that included a waterfall. What is the name of this house?": [
        "Fallingwater",
        "Watering Heights",
        "Mossyledge",
        "Taliesin"
    ]
}

FileName = 'questions.json'

try:
    with open(FileName, 'w') as file:
        json.dump(QUESTIONS, file, indent = 3)
        print("Done!")
except:
    print("Error")

