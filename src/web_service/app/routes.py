import requests

from flask import Blueprint, jsonify, Response, request

from app.database.container import categoryService, questionService
from app.utils.json_parser import JSONParser
from app.utils.validator import Validator


routes_blueprint = Blueprint('routes_blueprint', __name__)


@routes_blueprint.route('/api/get_questions', methods=['POST'])
def get_questions() -> Response:
    data = request.get_json()
    raw_questions_num = data['questions_num']

    try:
         questions_num = Validator.assert_positive_int_value(raw_questions_num)
    except Exception as e:
        return jsonify({'response': str(e)})

    try:
        json_data = requests.get(f'https://jservice.io/api/random?count={questions_num}').json()
    except Exception:
        return jsonify(None)

    response = {}

    for raw_question in json_data:
        while True:
            question_fields = ['id', 'question', 'answer', 'created_at']
            category_fields = ['id', 'title', 'created_at']

            question_data = JSONParser.read_json_data(raw_question, question_fields)
            category_data = JSONParser.read_json_data(raw_question['category'], category_fields)
            question_data['category_id'] = category_data['id']

            try:
                categoryService.create(category_data)
            except Exception:
                pass

            try:
                questionService.create(question_data)
                response = question_data
                break
            except Exception:
                raw_question = requests.get('https://jservice.io/api/random?count=1').json().pop()

    return jsonify(response)
