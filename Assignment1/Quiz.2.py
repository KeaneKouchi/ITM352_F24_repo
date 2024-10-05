# Create a quiz
# version 2
# Keane Kouchi
# 10/2/24

QUESTIONS = [
    ("What is the airspeed of an unladen swallow in miles per hour? ", "12"),
    ("What is the capital of Texas? ", "Austin"),
    ("The Last Supper was painted by which artist? ", "Da Vinci"),
    ("Who won Superbowl XXXIV", "Rams")

]

for question, CorrectAnswer in QUESTIONS:
    answer = input(f"{question}? ")
    if answer == CorrectAnswer:
        print("Correct!")
    else:
        print(f"The answer is {CorrectAnswer!r}, not {answer!r}")
