setup:
	pipenv install --dev
	pipenv shell

test:
	pytest --cov=app

run:
	python app.py
