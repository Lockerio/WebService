from typing import Type

from app.database.models import Category
from app.database.serializers.categories_serializer import CategorySerializer


class CategoryService:
    def __init__(self, serializer: CategorySerializer):
        self.serializer = serializer

    def get_one(self, category_id: int) -> Category:
        return self.serializer.get_one(category_id)

    def get_all(self) -> list[Type[Category]]:
        return self.serializer.get_all()

    def create(self, data: dict) -> Category:
        if self.get_one(data['id']):
            raise Exception('Такая категория уже существует!')
        return self.serializer.create(data)

    def update(self, data: dict) -> Category:
        category = self.serializer.get_one(data['id'])
        if category:
            return self.serializer.update(category)
        raise Exception('Категории с таким id не существует!')

    def delete(self, category_id: int):
        self.serializer.delete(category_id)
