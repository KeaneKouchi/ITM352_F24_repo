score_schema = {
    'type': 'object',
    'properties': {
        'user_id': {'type': 'string'},
        'category': {'type': 'string'},
        'score': {'type': 'integer'},
        'total_questions': {'type': 'integer'}
    },
    'required': ['user_id', 'category', 'score', 'total_questions']
}
