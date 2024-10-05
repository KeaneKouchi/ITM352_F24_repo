# Create a quiz game where each question has 4 possible answers
# make questions a dictionary
# allow user to select the correct answer by its label
# version 4
# Keane Kouchi
# 10/2/24

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

for question, alternatives in QUESTIONS.items():
    CorrectAnswer = alternatives[0]
    SortedAlternatives = sorted(alternatives)
    
    for label, alternative in zip(['a', 'b', 'c', 'd'], SortedAlternatives):
        print(f"{label}: {alternative}")
    
    AnswerLabel = input(f"{question} (a, b, c, d): ").strip().lower()
    
    if AnswerLabel in ['a', 'b', 'c', 'd']:
        answer_index = ['a', 'b', 'c', 'd'].index(AnswerLabel)
        answer = SortedAlternatives[answer_index]




#for question, alternatives in QUESTIONS.items():
#    CorrectAnswer = alternatives[0]
 #   SortedAlternatives = sorted(alternatives)
#
 #   for label, alternative in enumerate(SortedAlternatives):
  #      print(f"{label}: {alternative}")
#
 #   AnswerLabel = int(input(f"{question} "))
  #  answer = SortedAlternatives[AnswerLabel]

    #answer = input(f"{question}? ")
    #for alternative in sorted(alternatives):
    #    #print(f" - {alternative}")
    #answer = input(f"{question}? ")

    if answer == CorrectAnswer:
        print("Correct!")
    else:
        print(f"The answer is {CorrectAnswer!r}, not {answer!r}")