# Skeleton of quiz game (Assignment3)
#
# Keane Kouchi
# 11/6/24

from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

score = 0
question_num = 0
question_list = []

# Load the questions from the updated JSON file
with open("questions.json") as question_file:
    questions = json.load(question_file)
    question_list = list(questions.items())

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    global question_num, score
    if question_num >= len(question_list):
        return redirect(url_for("result"))

    current_question = question_list[question_num][0]
    options = question_list[question_num][1]

    if request.method == "POST":
        selected_answer = request.form.get("answer")

        # Define the correct answers manually
        correct_answers = {
            "What is the airspeed of an unladen swallow in miles/hr": "12",
            "What is the capital of Texas": "Austin",
            "The Last Supper was painted by which artist": "Da Vinci",
            "Which classic novel opens with the line 'Call Me Ishmael'?": "Moby Dick",
            "Frank Lloyd Wright designed a house that included a waterfall. What is the name of this house?": "Fallingwater"
        }

        # Update score if the answer is correct
        if selected_answer == correct_answers.get(current_question):
            score += 1

        # Move to the next question
        question_num += 1
        return redirect(url_for("quiz"))

    return render_template("quiz.html", question_num=question_num + 1,
                           question=current_question, options=options)

@app.route("/result")
def result():
    global score
    return render_template("result.html", score=score)

# Run the application in debug mode
if __name__ == "__main__":
    app.run(debug=True)
