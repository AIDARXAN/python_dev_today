# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED=1
ENV PORT 8000

WORKDIR /code
COPY requirements.txt /code/
RUN apt-get update && apt-get install -y cron
RUN service cron start
RUN pip install -r requirements.txt
COPY . /code/

CMD ./manage.py migrate && \
    ./manage.py collectstatic --noinput && \
    ./manage.py crontab add && \
    gunicorn main.wsgi:application --bind 0.0.0.0:$PORT
