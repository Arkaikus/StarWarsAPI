build:
	docker-compose -p "starwars_api" -f "./docker/docker-compose.yml" build api

run:
	docker-compose -p "starwars_api" -f "./docker/docker-compose.yml" up -d api

stop:
	docker-compose -p "starwars_api" -f "./docker/docker-compose.yml" stop api

push:
	docker-compose -p "starwars_api" -f "./docker/docker-compose.yml" push

dj-up:
	python app\manage.py runserver localhost:8080

dj-migrate:
	python app\manage.py makemigrations api allauth
	python app\manage.py makemigrations
	python app\manage.py migrate

dj-populate:
	python app\manage.py populate

deploy: stop run