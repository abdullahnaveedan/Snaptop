@echo off
code .
call env\Scripts\activate
python manage.py runserver
