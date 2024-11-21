import json, random

# Load questions from a JSON file
def LoadQuestions(filename):
    with open(filename, "r") as file:
        return json.load(file)

# Function for 50/50 hint
def FiftyFiftyHint(question, alternatives, correct_answer, used_hint):
    if used_hint:
        raise ValueError("Hint already used")
    wrong_answers = [alt for alt in alternatives if alt != correct_answer]
    one_wrong = random.sample(wrong_answers, 1)
    remaining_answers = [correct_answer] + one_wrong
    return remaining_answers, True
