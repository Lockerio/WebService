from sqlalchemy.orm import Session

from app.database.database import engine

from app.database.serializers.categories_serializer import CategorySerializer
from app.database.serializers.questions_serializer import QuestionSerializer

from app.database.services.categories_service import CategoryService
from app.database.services.questions_service import QuestionService


session = Session(bind=engine)

categorySerializer = CategorySerializer(session)
questionSerializer = QuestionSerializer(session)

categoryService = CategoryService(categorySerializer)
questionService = QuestionService(questionSerializer)
