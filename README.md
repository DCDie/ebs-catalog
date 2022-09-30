# 🛒 CATALOG API

REST API for Internet Catalog project.

### 📝 Requirements

1. Python 3.10
2. PostgreSQL

### 🔧 .env

```python
# DJANGO
SECRET_KEY=
DEBUG=True

# DATABASE
NAME=
USER=
PASSWORD=
HOST=
PORT=
```

### 📦️ Commands

```
python manage.py update_products
```

#### Run tests

```shell
# Run flake8 test
tox -e flake8
# Run django tests with coverage
tox -e django41
```

#### Deployment

``` python
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
