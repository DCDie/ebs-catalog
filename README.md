# 📱 CATALOG API

REST API for Internet Catalog project.

### 📝 Requirements

1. Python 3.10
2. PostgreSQL
3. Celery

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

```
python manage.py test
```

#### Deployment

``` python
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
