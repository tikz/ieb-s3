FROM python:3.10-alpine

RUN apk add bash
RUN pip install pipenv

RUN mkdir -p /iebs3
COPY . /iebs3/
WORKDIR /iebs3
RUN  pipenv install --system --deploy

EXPOSE 80
CMD python manage.py migrate && trap 'killall python; killall -s KILL gunicorn' INT && python manage.py update_prices & gunicorn --chdir iebs3 --bind :80 --timeout 120 --workers=3 --threads=3 --worker-connections=1000 iebs3.wsgi:application