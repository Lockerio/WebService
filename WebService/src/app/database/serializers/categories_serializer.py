from typing import List, Type

from sqlalchemy.orm import Session

from app.database.models import Category


class CategorySerializer:
    def __init__(self, session: Session):
        self.session = session

    def get_one(self, category_id: int) -> Category:
        return self.session.query(Category).get(category_id)

    def get_all(self) -> list[Type[Category]]:
        return self.session.query(Category).all()

    def create(self, data: dict) -> Category:
        category = Category(**data)
        self.session.add(category)
        self.session.commit()
        return category

    def update(self, category: Category) -> Category:
        self.session.add(category)
        self.session.commit()
        return category

    def delete(self, category_id: int):
        category = self.get_one(category_id)
        self.session.delete(category)
        self.session.commit()
