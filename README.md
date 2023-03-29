# IEB (S3)

## Run

### Local
```
pip install pipenv
pipenv install
pipenv shell

python manage.py migrate

python manage.py runserver

python manage.py update_prices
```

### Ejemplo instancia Docker
```
docker run -p 9090:80 ghcr.io/tikz/ieb-s3:main
```