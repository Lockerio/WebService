import requests

from flask import Blueprint, jsonify, Response, request

from app.database.container import categoryService, questionService
from app.utils.formatter import Formatter
from app.utils.json_parser import JSONParser
from app.utils.validator import Validator


routes_blueprint = Blueprint('routes_blueprint', __name__)


@routes_blueprint.route('/api/get_saved_categories')
def get_saved_categories() -> Response:
    categories = categoryService.get_all()
    categories_JSON = Formatter.format_list_of_objects_to_dict(categories,
                                                               Formatter.format_category_data_to_dict)
    return jsonify(categories_JSON)


@routes_blueprint.route('/api/get_saved_questions')
def get_saved_questions() -> Response:
    questions = questionService.get_all()
    questions_JSON = Formatter.format_list_of_objects_to_dict(questions,
                                                              Formatter.format_question_data_to_dict)
    return jsonify(questions_JSON)


@routes_blueprint.route('/api/request_questions', methods=['POST'])
def request_questions() -> Response:
    data = request.get_json()
    try:
        raw_questions_num = data['questions_num']
        questions_num = Validator.assert_positive_int_value(raw_questions_num)
    except KeyError:
        return jsonify({'response': 'Вы не указали "questions_num" в теле запроса!'})
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
