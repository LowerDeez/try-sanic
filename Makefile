init:
	pipenv --python 3.6; \
	pipenv install; \

run:
	python main.py

# alembic revision -m "Migration message" --autogenerate --head head
revision:
	alembic revision --autogenerate

upgrade:
	alembic upgrade head

downgrade:
	alembic downgrade head