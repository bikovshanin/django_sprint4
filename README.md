# Веб-приложение для публикации постов «Blogicum»

## _Описание проекта:_

#### **_*Blogicum*_ - сервис для публикации постов и комментариев к ним.**


### _Технологии:_

[![pre-commit](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)](https://www.python.org/downloads/release/python-3111/)
[![pre-commit](https://img.shields.io/badge/Django-3.2-092E20?logo=django&logoColor=white)](https://docs.djangoproject.com/en/4.2/releases/3.2/)


### _Возможности проекта:_
* регистрация пользователей
* возможность добавления/редактирования/удаления своих публикаций
* просмотр публикаций других пользователей
* возможность добавления комментариев к публикациям
* добавление к публикациям фото
* просмотр публикаций в разрезе категорий и локаций 

### _Запуск проекта:_
- Склонировать репозиторий:
```
https://github.com/bikovshanin/django_sprint4.git
```
- Создать и активировать виртуальное окружение:
```
python3 -m venv venv
source venv/bin/activate
```
- Обновить pip:
```
python3 -m pip install --upgrade pip
```
- Установить библиотеки:
```
pip install -r requirements.txt
```
- Выполнить миграции:
```
python3 blogicum/manage.py migrate
```
- Загрузить фикстуры DB:
```
python3 blogicum/manage.py loaddata db.json
```
- Создать суперпользователя:
```
python3 blogicum/manage.py createsuperuser
```
- Запустить сервер django:
```
python3 blogicum/manage.py runserver
```
##
### _Демо-версия проекта:_
[Blogicum](http://bikovshanin.pythonanywhere.com)

##
