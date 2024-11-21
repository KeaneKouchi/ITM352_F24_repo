from flask import Blueprint, jsonify, request
from datetime import datetime
from shared_data import QUESTIONS
api = Blueprint('api', __name__)

# In-memory storage (replace with database in production)
scores_db = []

@api.route('/api/questions/<category>', methods=['GET'])
def get_questions(category):
    try:
        questions = QUESTIONS.get(category, {})
        return jsonify({
            'status': 'success',
            'data': questions
        }), 200
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@api.route('/api/scores', methods=['POST'])
def save_score():
    data = request.get_json()
    score = {
        'user_id': data.get('user_id'),
        'category': data.get('category'),
        'score': data.get('score'),
        'total_questions': data.get('total_questions'),
        'timestamp': datetime.now().isoformat()
    }
    scores_db.append(score)
    return jsonify({
        'status': 'success',
        'message': 'Score saved successfully'
    }), 201

@api.route('/api/scores', methods=['GET'])
def get_scores():
    return jsonify({
        'status': 'success',
        'data': scores_db
    }), 200
