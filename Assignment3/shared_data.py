import QuizFunctions as QF

try:
    QUESTIONS = QF.LoadQuestions("questions.json")
    categories = list(QUESTIONS.keys())
except Exception as e:
    print(f"Failed to initialize quiz: {str(e)}")
    QUESTIONS = {}
    categories = []
