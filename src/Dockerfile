FROM python:3.11

ENV PYTHONUNBUFFERED 1

WORKDIR /web_service

COPY web_service/requirements.txt .

RUN pip install --upgrade pip &&  python -m pip install -r requirements.txt

COPY /web_service/alembic ./alembic
COPY /web_service/app ./app
COPY /web_service/alembic.ini .
