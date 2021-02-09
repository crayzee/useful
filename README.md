<h2 align="center">Useful</h2>


### Описание проекта:
Скоро

### Инструменты разработки

**Стек:**
- Python >= 3.8
- FastAPI == 0.63.0
- PostgreSQL

**Ссылки**:

## Старт

#### 1) Создать образ

	docker-compose build
	
##### 2) Запустить контейнер

	docker-compose up
	
##### 3) Перейти по адресу

	http://127.0.0.1:8000/docs
	
## Разрабока

##### 1) Сделать форк репозитория и поствить звездочку)

##### 2) Клонировать репозиторий

	git clone ссылка_сгенерированная_в_вашем_репозитории
	

##### 3) Установить poetry

	curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
	
[help docs](https://python-poetry.org/docs)

##### 4) Установить зависимости

	poetry install
	
##### 5) В папке 'src.config' файл 'local_config.py-exp' переименовать в 'local_config.py' и прописать коннект к базе

##### 6) Активировать виртуальное окружение

	poetry shell
	
##### 7) Создание миграций

	poetry run alembic revision --autogenerate
	
##### 8) Применить миграции
		
	poetry run alembic upgrade head
	
##### 9) Создать суперпользователя

	в разработке
	
##### 10) Запустить сервер

	uvicorn main:app --reload
	
##### 11) Перейти по адресу

	http://127.0.0.1:8000/docs
	
## Licence

[BSD 3-Clause Licence](https://opensource.org/licenses/BSD-3-Clause)

Copyright (c) 2021-present, DJWOMS