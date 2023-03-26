FROM python:3.10-alpine

RUN apk add bash

RUN mkdir -p /iebs3
COPY . /iebs3/
WORKDIR /iebs3

RUN pip install pipenv && pipenv install --dev --system --deploy

EXPOSE 80
CMD python manage.py migrate && trap 'killall python; killall -s KILL gunicorn' INT && python manage.py update_prices & gunicorn --chdir iebs3 --bind :80 iebs3.wsgi:application