from typing import List, Type

from sqlalchemy.orm import Session

from app.database.models import Question


class QuestionSerializer:
    def __init__(self, session: Session):
        self.session = session

    def get_one(self, question_id: int) -> Question:
        return self.session.query(Question).get(question_id)

    def get_all(self) -> list[Type[Question]]:
        return self.session.query(Question).all()

    def create(self, data: dict) -> Question:
        question = Question(**data)
        self.session.add(question)
        self.session.commit()
        return question

    def update(self, question: Question) -> Question:
        self.session.add(question)
        self.session.commit()
        return question

    def delete(self, question_id: int):
        question = self.get_one(question_id)
        self.session.delete(question)
        self.session.commit()
