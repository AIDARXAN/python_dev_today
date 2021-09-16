# Установка и запуск через Докер

### Примечание
Для форматирования и линтинга кода были использованы библиотеки
Black и Flake8 соответсвенно. Но между ними был конфликт,
например даже после форматирования при помощи Black, Flake8 показывал что в некоторых местах есть ошибки,
так решил оставить форматирование от Black и нескольких местах Flake8 не прошел. 

Для легкой установки рекомендую использовать докер так как это займет
намного меньше шагов и времени чем ручная настройка окружения. 
[Инструкция по установке докера](https://docs.docker.com/compose/install/)

Склонируйте проект:
```
git clone https://github.com/AIDARXAN/python_dev_today.git
```
Откройте терминал и введите команды:
```
cd path/to/project/where/you/cloned/python_test_assessment
cp .env.example .env  
docker-compose up -d --build
```
Можно теперь пользоваться в браузере или через постман по адресу http://127.0.0.1:8000

## Документация Постман
[Дока по апишке](https://documenter.getpostman.com/view/6954620/U16oqPYM)

## Адрес Heroku
[https://python-test-assessment.herokuapp.com/](https://python-test-assessment.herokuapp.com/)

# Установка и запуск через Вручную Linux
Если вам лень устанавливать докер, но вам не лень сделать шаги которые описаны ниже, поздравляю вы совсем не ленивый)

## Установка базы данных
Выберите операционную систему которая установлена у вас и следуйте инструкциям
[https://www.postgresql.org/download/](https://www.postgresql.org/download/)


## Настройка базы данных

Для создания базы данных нужно ввести следующие команды

`sudo su - postgres` заходим за root пользователя

`psql` открываем postgresql консоль

`CREATE DATABASE myproject;` создаем базу данных

`CREATE USER myprojectuser WITH PASSWORD 'password';` создаем пользователя

`GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;` даем все разрешения новому пользователю к созданной базе

## Связь приложения и базы

Создайте файл ".env" корневой папке, в нем будут определены все переменные которые нужны для связи базы данных и Django приложения

В файле укажите данные созданной ранее базы и пользователя посмотрев пример в файле ".env.example"
В переменную **DB_HOST** впишите значение **localhost**

## Создание виртуального окружения
```
python -m venv python-test 
source python-test/bin/activate          
pip install -r requirements.txt
apt-get update && apt-get install -y cron
```

## Прогон миграций и запуск
```
./manage.py migrate
./manage.py crontab add
./manage.py runserver
```

