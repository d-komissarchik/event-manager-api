FROM python:3.11-slim

WORKDIR /app

COPY ./requirements.txt /code/requirements.txt

RUN pip install --user --no-cache-dir -r /code/requirements.txt


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /app/

CMD ["gunicorn", "Event_manager.wsgi:application", "--bind", "0.0.0.0:8000"]