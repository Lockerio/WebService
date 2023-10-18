from sqlalchemy import Column, Integer, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship

from app.database.database import Base


class Category(Base):
    __tablename__ = 'Category'
    id = Column(Integer(), primary_key=True, nullable=False, autoincrement=True)
    title = Column(Text(), nullable=False)
    created_at = Column(DateTime(), nullable=False)

    questions = relationship("Question", back_populates="category")

    def __repr__(self):
        return f'{self.title}'


class Question(Base):
    __tablename__ = 'Question'
    id = Column(Integer(), primary_key=True, nullable=False, autoincrement=True)
    question = Column(Text(), nullable=False)
    answer = Column(Text(), nullable=False)
    created_at = Column(DateTime(), nullable=False)
    category_id = Column(Integer(), ForeignKey('Category.id'))

    category = relationship("Category", back_populates="questions")

    def __repr__(self):
        return f'{self.question}'
