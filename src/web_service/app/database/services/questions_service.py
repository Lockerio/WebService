from typing import Type

from app.database.models import Question
from app.database.serializers.questions_serializer import QuestionSerializer


class QuestionService:
    def __init__(self, serializer: QuestionSerializer):
        self.serializer = serializer

    def get_one(self, question_id: int) -> Question:
        return self.serializer.get_one(question_id)

    def get_all(self) -> list[Type[Question]]:
        return self.serializer.get_all()

    def create(self, data: dict) -> Question:
        if self.get_one(data['id']):
            raise Exception('Такой вопрос уже существует!')
        return self.serializer.create(data)

    def update(self, data: dict) -> Question:
        question = self.serializer.get_one(data['id'])
        if question:
            return self.serializer.update(question)
        raise Exception('Вопроса с таким id не существует!')

    def delete(self, question_id: int):
        self.serializer.delete(question_id)
