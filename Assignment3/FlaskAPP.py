# Notes on AI- AI used for the entirety of RESTful API implementation and for the style (CSS and Javascript)
# Most error validation added with ChatGPT with prompt "Add python built in data validation and error handling"
# All the QuizFunctions functions were from my previous Assignment1 copied over
# Also reused my Assignment1 questions.json that was already set up for categories
# Function/section specific AI usage noted in comment in respective section


from flask import Flask, render_template, request, redirect, url_for, session
import random
import time
import QuizFunctions as QF
from api import api
from shared_data import QUESTIONS, categories

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.register_blueprint(api)

@app.route('/')
def index():
    try:
        if not categories:
            raise ValueError("No quiz categories available")
        return render_template('index.html', categories=categories)
    except Exception as e:
        return render_template('error.html', message="Failed to load quiz categories")

@app.route('/quiz/<category>', methods=['GET', 'POST'])
def quiz(category):
    try:
        if category not in QUESTIONS:
            return redirect(url_for('index'))

        # Initialize session variables
        if 'questions_list' not in session or session['category'] != category:
            if not QUESTIONS[category]:
                raise ValueError(f"No questions available for category: {category}")
            session['category'] = category
            session['start_time'] = time.time()
            questions_list = [(q, a) for q, a in QUESTIONS[category].items()]
            random.shuffle(questions_list)
            
            # ChatGPT with prompt (used my old Assignment1 quiz as template) modify to enumerate instead of using
            # a hard coded list of letters and randomize the order of the questions and alternatives
            # Shuffle alternatives once during initialization and store the shuffled order
            for i, (question, data) in enumerate(questions_list):
                correct_answer = data['alternatives'][0]
                shuffled_alternatives = data['alternatives'][:]
                random.shuffle(shuffled_alternatives)
                questions_list[i] = (question, {
                    'alternatives': shuffled_alternatives,
                    'correct_index': shuffled_alternatives.index(correct_answer),
                    'explanation': data['explanation']
                })
                
            session['questions_list'] = questions_list
            session['total_correct'] = 0
            session['used_hint'] = False
            session['current_question_index'] = 0

        if session['current_question_index'] >= len(session['questions_list']):
            return redirect(url_for('result', category=category))

        # Handle answer submission
        if request.method == 'POST':
            if 'answer_status' in request.form:
                session['current_question_index'] += 1
                session['used_hint'] = False
                
                if session['current_question_index'] >= len(session['questions_list']):
                    return redirect(url_for('result', category=category))
                
                question, data = session['questions_list'][session['current_question_index']]
                labeled_answers = enumerate(data['alternatives'])
                return render_template('quiz.html',
                    question=question,
                    labeled_answers=labeled_answers,
                    category=category,
                    answer_status=None,
                    explanation=None,
                    current_question_number=session['current_question_index'] + 1,
                    used_hint=session['used_hint']
                )

            if 'answer' not in request.form:
                question, data = session['questions_list'][session['current_question_index']]
                labeled_answers = enumerate(data['alternatives'])
                return render_template('quiz.html',
                    question=question,
                    labeled_answers=labeled_answers,
                    category=category,
                    answer_status=None,
                    explanation=None,
                    current_question_number=session['current_question_index'] + 1,
                    used_hint=session['used_hint'],
                    error="Please select an answer"
                )

            answer = request.form.get('answer')
            if not answer:
                question, data = session['questions_list'][session['current_question_index']]
                labeled_answers = enumerate(data['alternatives'])
                return render_template('quiz.html',
                    question=question,
                    labeled_answers=labeled_answers,
                    category=category,
                    answer_status=None,
                    explanation=None,
                    current_question_number=session['current_question_index'] + 1,
                    used_hint=session['used_hint'],
                    error="Please select an answer"
                )

            question, data = session['questions_list'][session['current_question_index']]
            alternatives = data['alternatives']
            correct_index = data['correct_index']

            # Handle 50/50 hint
            if answer == '50':
                if session['used_hint']:
                    return render_template('quiz.html',
                        question=question,
                        labeled_answers=enumerate(alternatives),
                        category=category,
                        answer_status=None,
                        explanation=None,
                        current_question_number=session['current_question_index'] + 1,
                        used_hint=session['used_hint'],
                        error="Hint already used for this question"
                    )
                correct_answer = alternatives[correct_index]
                alternatives, session['used_hint'] = QF.FiftyFiftyHint(
                    question, alternatives, correct_answer, session['used_hint']
                )
                correct_index = alternatives.index(correct_answer)
                data['alternatives'] = alternatives
                data['correct_index'] = correct_index
                session['questions_list'][session['current_question_index']] = (question, data)
                labeled_answers = enumerate(alternatives)
                return render_template('quiz.html',
                    question=question,
                    labeled_answers=labeled_answers,
                    category=category,
                    answer_status=None,
                    explanation=None,
                    current_question_number=session['current_question_index'] + 1,
                    used_hint=session['used_hint']
                )
            # Validate answer
            valid_answer_range = [str(i) for i in range(len(alternatives))]
            if answer not in valid_answer_range:
                return render_template('quiz.html',
                    question=question,
                    alternatives=alternatives,
                    error=f"Invalid answer. Please choose a valid option (0 - {len(alternatives)-1}).",
                    category=category,
                    answer_status=None,
                    explanation=None,
                    current_question_number=session['current_question_index'] + 1,
                    used_hint=session['used_hint']
                )

            # Check answer
            selected_answer_index = int(answer)
            if selected_answer_index == correct_index:
                session['total_correct'] += 1
                answer_status = "Correct!"
            else:
                answer_status = "Incorrect!"

            return render_template('quiz.html',
                question=question,
                alternatives=alternatives,
                explanation=data['explanation'],
                answer_status=answer_status,
                category=category,
                current_question_number=session['current_question_index'] + 1,
                used_hint=session['used_hint'],
                correct_index=correct_index,
                selected_index=selected_answer_index,
                labeled_answers=enumerate(alternatives)
            )

        # Display current question (GET request)
        question, data = session['questions_list'][session['current_question_index']]
        labeled_answers = enumerate(data['alternatives'])
        current_question_number = session['current_question_index'] + 1
        
        return render_template('quiz.html',
            question=question,
            labeled_answers=labeled_answers,
            category=category,
            answer_status=None,
            explanation=None,
            current_question_number=current_question_number,
            used_hint=session['used_hint']
        )
    except Exception as e:
        return render_template('error.html', message="An error occurred during the quiz")

@app.route('/result')
def result():
    try:
        if 'total_correct' not in session or 'questions_list' not in session:
            raise ValueError("No quiz session found")
            
        total_correct = session['total_correct']
        total_questions = len(session['questions_list'])
        category = session['category']
        
        # Calculate total time
        end_time = time.time()
        total_time = int(end_time - session['start_time'])
        minutes = total_time // 60
        seconds = total_time % 60

        return render_template('result.html', 
                             total_correct=total_correct, 
                             category=category, 
                             total_questions=total_questions,
                             minutes=minutes,
                             seconds=seconds)
    except Exception as e:
        return render_template('error.html', message="Failed to display results")

# ChatGPT with prompt (existing code looped back to the same category selection screen as the Select Another Category button)
# "Modify this to start the quiz over in the same category"    
@app.route('/play-again')
def play_again():
    try:
        category = session.get('category')
        session.clear()
        if category:
            return redirect(url_for('quiz', category=category))
        return redirect(url_for('index'))
    except Exception as e:
        return render_template('error.html', message="Failed to restart quiz")

if __name__ == '__main__':
    app.run(debug=True)
