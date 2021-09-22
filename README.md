# StarWarsAPI

This simple API lets you manage characters from star wars

## Setup

- Download the repo with `git clone`
- Create a virtualenv with `virtualenv venv -p python3`
- Activate virtualenv
- Install requirements with `pip install -r requirements.txt`
- Check Makefile
- Run migrations with `make dj-migrate`
- Populate db with  `make dj-populate`
  - Executes custom command to fetch data from [swapi.dev](https://swapi.dev/)
  - Fixtures at `app\api\fixtures` but django has utf-8 encoding problems
  - db.sqlite already populated
- Run app with `make dj-up`
- Go to `localhost:8080/doc` for swagger documentation and openapi schema
- Credentials user=root, password=root if fixtures loaded or sign up

### Docker

Required docker and docker-compose

Run `make build` to create the docker image, then run `make run` to start the container of the api

the container runs on port `9080` feel free to change it in `docker/docker-compose-yml`

## Endpoints

Check `host:port/doc` for swagger documentation

## Licence

MIT License  
Check the LICENCE file