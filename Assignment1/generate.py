# Given the input of a student number, generate two integers
# indicating the questions that a student needs to answer
# Keane Kouchi
# 10/2/24


def GenerateNumbers(StudentId, NumQuestions):
    # remove any non numeric characters
    ID = ''.join(filter(str.isdigit, StudentId))

    # check that student id is valid (8 digits)
    if len(ID) != 8:
        raise ValueError("Invalid student ID: it should be 8 digits")
    
    # use a simple algo to generate two unique numbers from 1 to N_QUESTIONS
    SumDigits = sum(int(digit) for digit in ID)
    first = (SumDigits % 7) + 1

    #calculate the second number using the product of the digits
    product = 1
    for digit in ID:
        if(int(digit) != 0):
            product *= int(digit)
    second = (product % 7) + 1

    while first == second:
        second = (second % 7) + 1
    return first, second
    
try: 
    N_QUESTIONS = 10
    StudentId = input("Enter your student ID number (XXX-XX-XXX): ")
    num1, num2 = GenerateNumbers(StudentId, N_QUESTIONS)
    print(f"Your two assignments are {num1} and {num2}")

except ValueError as e:
    print(f"Error {e}")