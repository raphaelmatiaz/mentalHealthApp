help: ## Show help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n",$$1,$$2}'

migrate:  ## Run migrations
	docker compose run -v postgres:/Users/santiagopereira/EticProgramação/BaseDeDados/mentalHealthApp/django-app -it django-app poetry run python3 manage.py makemigrations

build: migrate  ## Build the project
	docker build -t django-app -f ops/django-app.Dockerfile ./django-app

bash:  ## Run bash in the django-app container
	docker compose exec -it django-app bash

up:  ## Run the project
	docker compose up --build

dump:  ## Dump the database
	docker compose exec -it django-app poetry run python manage.py dumpdata -o data.json
	docker cp mentalhealthapp-django-app-1:/app/data.json ./data.json

load:  ## Load the database
	docker compose exec -it django-app poetry run python manage.py loaddata /app/data.json

up-database:  ## Docker compose up database only
	docker compose up -d --build database || true

local: up-database  ## Runserver local
	cd django-app && poetry run python manage.py runserver
connect: ## Connect to the Postgres database
	docker compose exec -it database psql --username=user --dbname=db

sql: ## Run scripts/insert_users_and_orders.sql script
	docker compose exec database psql --username=user --dbname=db -f /docker-entrypoint-initdb.d/insert_into_categories.sql
	docker compose exec database psql --username=user --dbname=db -f /docker-entrypoint-initdb.d/insert_into_phrases.sql
	
