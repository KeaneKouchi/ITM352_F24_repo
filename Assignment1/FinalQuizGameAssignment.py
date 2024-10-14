# Final quiz Assignment 
# I'm assigned additional requirements 5 and 7, I also chose to do 10
# 5: Allow the user to choose a category for their questions
# 7: Add explanations for why the correct answer is the correct answer.
# 10: Add a 50/50 feature (eliminating 2 of the 4 answers, wrong ones that is) that can only be used once per game instance.

# Please refer to questions.json and QuizFunctions.py (where my functions are stored)

# Keane Kouchi
# 10/13/24


import random
import QuizFunctions as QF

# Load the questions json (refer to QuizFunctions.py)
QUESTIONS = QF.LoadQuestions("questions.json")
categories = list(QUESTIONS.keys())

while True:
    # Allow for choosing a category (refer to QuizFunctions.py)
    SelectedCategory = QF.UserCategorySelection(categories)

    QuestionsList = [(question, alternatives) for question, alternatives in QUESTIONS[SelectedCategory].items()]
    
    # Randomize the order of the questions
    random.shuffle(QuestionsList)

    TotalCorrect = 0
    # Initializing as the number of questions and minusing 1 for every incorrect (the first attempt)
    CorrectFirstTry = len(QuestionsList)
    # Hint can only be used once, variable necessary to keep track
    UsedHint = False

    for question, data in QuestionsList:
        # Stores the correct answer prior to shuffling
        alternatives = data["alternatives"]
        CorrectAnswer = alternatives[0]  
        # Randomize the order of the answers
        random.shuffle(alternatives)
        # Keeps track of whether it's the first attempt at answering
        FirstTry = True
        # Used to only apply the a/b valid input to the specific question the hint is used on
        HintForCurrentQuestion = False

        # Keeps reasking the question until receiving the correct answer
        while True:
            # The reminder about the hint only shows if it's not used yet
            if not UsedHint:
                print("Enter '50' to use your 50/50 hint (You may only use once!)")
            print(question)

            for label, alternative in zip(["a", "b", "c", "d"], alternatives):
                print(f"{label}: {alternative}")

            # Stores the user's response to the question
            AnswerLabel = input("Response: ").strip().lower()

            # Determine valid inputs based on whether the hint is in use
            if HintForCurrentQuestion:
                ValidAnswerLabels = ["a", "b"]
            else:
                ValidAnswerLabels = ["a", "b", "c", "d"]

            if AnswerLabel not in ValidAnswerLabels and AnswerLabel != "50":
                print(f"Invalid input, please choose from {', '.join(f'\'{label}\'' for label in ValidAnswerLabels)}. \n")
                continue
            
            if AnswerLabel == "50":
                if not UsedHint:
                    # Calls the 50/50 hint function from QuizFunctions.py
                    alternatives, UsedHint = QF.FiftyFiftyHint(question, alternatives, CorrectAnswer, UsedHint)
                    HintForCurrentQuestion = True  # Indicate the hint is currently in use
                else:
                    print("Sorry, you may only use the 50/50 hint one time. \n")
                continue
            
            if AnswerLabel in ValidAnswerLabels:
                AnswerIndex = ["a", "b", "c", "d"].index(AnswerLabel)
                answer = alternatives[AnswerIndex]

                # Checks if the answer is correct and adds 1 to total correct if it is
                if answer == CorrectAnswer:
                    print(f"Correct! {data['explanation']} \n")
                    TotalCorrect += 1
                    break
                else:
                    print("Incorrect, please try again. \n")
                if FirstTry:
                    CorrectFirstTry -= 1
                    # After minusing 1 from the total amount of questions, marks false
                    # so it doesn't count the next right answer for the same question
                    FirstTry = False

    print(f"You got {TotalCorrect} out of {len(QuestionsList)} correct.")
    # Added this because the total correct will always be 5 out of 5 unless ended early 
    # due to the program looping until a correct answer is given
    print(f"You got {CorrectFirstTry} correct on the first try!")

    # Function asks if the user wants to play again (refer to QuizFunctions.py)
    if not QF.PlayAgainOrNah():
        print("Thanks for playing! \n")
        break
