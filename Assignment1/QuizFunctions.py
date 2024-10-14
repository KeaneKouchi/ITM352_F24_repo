# functions used for Quiz game / Assignment 1

import json, random

# Function for user category selection
def UserCategorySelection(categories):
    while True:
        print("Please choose a category ('a','b','c').")
        for choice, category in zip(["a", "b", "c"], categories):
            print(f"{choice}: {category}")
        # simplifies to accept upper or lower case
        CategoryChoice = input("Response: ").strip().lower()
        
        if CategoryChoice not in ["a", "b", "c"]:
            print("Invalid input, please choose from 'a','b','c'.")
            continue
        
        ChoiceIndex = ["a", "b", "c"].index(CategoryChoice)
        print(f"You selected '{categories[ChoiceIndex]}'. \n")
        return categories[ChoiceIndex]


# Function for loading the questions into the quiz
def LoadQuestions(filename):
    with open(filename, "r") as file:
        return json.load(file)
    

# Function for the one time use 50/50 hint feature
def FiftyFiftyHint(question, alternatives, CorrectAnswer, UsedHint):
    if UsedHint:
        print("Sorry, you may only use the 50/50 hint one time. \n")
        return alternatives, UsedHint

    WrongAnswers = [alt for alt in alternatives if alt != CorrectAnswer]
    # Randomly select 1 wrong answer to display with the correct answer
    OneWrong = random.sample(WrongAnswers, 1)
    # Create new options with only 2 remaining answers
    RemainingAnswers = [CorrectAnswer] + OneWrong
    print("Using 50/50... \n")
    # Return the updated answers and mark the hint as used
    return RemainingAnswers, True


# Function for user choosing to keep playing or end the game    
def PlayAgainOrNah():
    while True:
        PlayOrQuit = input("Do you want to try another category? (yes/no): ").strip().lower()
        if PlayOrQuit in ["yes", "no"]:
            return PlayOrQuit == "yes"
        else:
            print("Invalid input, please answer (yes/no).")