# 📱 CATALOG API

REST API for Internet Catalog project.

### 📝 Requirements

1. Python 3.10
2. PostgreSQL
3. Celery

### 🔧 .env

```python
# DJANGO
SECRET_KEY="django-insecure-ivvj9!#yngyy+ivx(t&m*a0n@6b*kc38^0v3ew0g06-!x_pwih"
DEBUG=True

# DATABASE
NAME="ebs-catalog"
USER="ebs_user"
PASSWORD="ebs_password"
HOST=185.181.231.43
PORT=5432
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
