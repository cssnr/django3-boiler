[![Discord](https://img.shields.io/discord/899171661457293343?color=7289da&label=discord&logo=discord&logoColor=white&style=flat)](https://discord.gg/wXy6m2X8wY)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/dbceb84a912b4722a55d9cb0f2fcdc54)](https://www.codacy.com/gh/cssnr/django3-boiler/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=cssnr/django3-boiler&amp;utm_campaign=Badge_Grade)
# Django Boiler

Django 3.2 Boiler Plate using Bootstrap 5, Celery 5 and much more...

[https://sapps.me/](https://sapps.me/)

## Development

### manage.py

Using manage.py for web development

```text
git clone https://github.com/cssnr/django3-boiler.git
cd django3-boiler
cp settings.env.example settings.env
vim settings.env
IFS=$'\n';export env $(cat settings.env);IFS=' '
cd app
python -m venv venv
source venv/bin/activate
pip install -U pip
pip install -Ur requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver_plus 0.0.0.0:8000
```

### docker-compose

Using docker-compose up for stack development

```text
git clone https://github.com/cssnr/django3-boiler.git
cd django3-boiler
cp settings.env.example settings.env
vim settings.env
docker-compose up --remove-orphans --build -d
docker exec -it django3-boiler_app_1 sh
python manage.py makemigrations
python manage.py migrate
```
