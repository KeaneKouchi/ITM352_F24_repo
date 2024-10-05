# Create a quiz
# version 1
# Keane Kouchi
# 10/2/24


answer = input("What is the airspeed of an unladen swallow in miles per hour? ")

if answer == "12":
    print("Correct!")
else:
    print(f"The answer is '12', not {answer!r}")


answer = input("What is the capital of Texas? ")

if answer == "Austin":
    print("Correct!")
else:
    print(f"The answer is 'Austin', not {answer!r}")




QuestionsDict = {

     "What is the airspeed of an unladen swallow in miles per hour?": [
          "12",
          "8",
          "11",
          "15"
     ],
     "What is the capital of Texas": [
          "Austin",
          "San Antonio",
          "Dallas",
          "Waco"
     ],
     "The Last Supper was painted by which artist": [
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

