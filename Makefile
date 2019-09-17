setup:
	@echo "Boostrapping docker container..."
	docker-compose up -d

pip:
	docker-compose exec jupyter-notebook pipenv install --system --dev

app: setup
	@echo "Running app.py"
	docker-compose exec jupyter-notebook python3 app.py

test: setup
	docker-compose exec jupyter-notebook pytest --cov=app

shell: setup
	docker-compose exec -u $$(id -u):$$(id -g) jupyter-notebook bash

