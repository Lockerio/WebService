from typing import Dict, Any, List, Union, Callable

from app.database.models import Question, Category


class Formatter:
    @staticmethod
    def format_question_data_to_dict(question_data: Question) -> Dict[str, Any]:
        dict_data = {
            'id': question_data.id,
            'question': question_data.question,
            'answer': question_data.answer,
            'created_at': question_data.created_at,
            'category_id': question_data.category_id
        }
        return dict_data

    @staticmethod
    def format_category_data_to_dict(category_data: Category) -> Dict[str, Any]:
        dict_data = {
            'id': category_data.id,
            'title': category_data.title,
            'created_at': category_data.created_at
        }
        return dict_data

    @staticmethod
    def format_list_of_objects_to_dict(
            objects: List[Union[Question, Category]],
            func: Callable[[Union[Category, Question]], Dict]
    ) -> Dict:
        objects_dict = {
            'amount': len(objects),
            'objects': [
                func(obj) for obj in objects
            ]
        }
        return objects_dict
