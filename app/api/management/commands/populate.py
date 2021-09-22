# import logging
import requests
import traceback
from django.core.management.base import BaseCommand
from pprint import pprint
from api.models import Character, Planet, Film


class Command(BaseCommand):
    help = 'Populate db from swapi.dev'

    def handle(self, *args, **options):
        try:
            print("FETCHING CHARACTERS")
            endpoint = "https://swapi.dev/api/people"
            while True:
                _json = requests.get(endpoint).json()
                characters = _json['results']
                for character in characters:                    
                    _id = _url = character.get('url')\
                        .lstrip("https://swapi.dev/api/people/")\
                        .rstrip("/")                    
                    _name = character.get('name')
                    _character = Character(id=_id, name=_name)
                    _character.save()
                    print(f"Saved {_name} with id {_id}")

                endpoint = _json.get('next', None)
                if _json.get('next', None) is None:
                    break

                print(f"Fetching next page {endpoint}")

            print("Finished saving characters")
        except:
            traceback.print_exc()

        try:
            print("FETCHING PLANETS")
            endpoint = "https://swapi.dev/api/planets/"
            while True:
                _json = requests.get(endpoint).json()
                planets = _json['results']
                for planet in planets:
                    _id = planet.get('url')\
                        .lstrip("https://swapi.dev/api/planets/")\
                        .rstrip('/')
                    _name = planet.get('name')
                    _planet = Planet(id=_id, name=_name)
                    _planet.save()
                    print(f"Saved {_name} with id {_id}")

                endpoint = _json.get('next', None)
                if _json.get('next', None) is None:
                    break

                print(f"Fetching next page {endpoint}")
            print("Finished saving planets")
        except:
            traceback.print_exc()

        try:
            print("FETCHING FILMS")
            endpoint = "https://swapi.dev/api/films/"
            films = requests.get(endpoint).json()['results']
            for film in films:
                _id = film.get('url').lstrip(endpoint).rstrip('/')
                title = film.get('title')
                prelude = film.get('opening_crawl', '')
                film_characters = film.get('characters', [])
                film_planets = film.get('planets', [])
                film = Film(id=_id, title=title, prelude=prelude)
                film.save()
                print(f"Saved {title} with id {_id}")

                print("Related characters")
                for film_character in film_characters:
                    film_character_id = film_character \
                        .lstrip("https://swapi.dev/api/people/") \
                        .rstrip('/')

                    try:
                        print(f"character id {film_character_id}")
                        _character = Character.objects.get(
                            pk=film_character_id)
                        film.characters.add(_character)
                    except:
                        print(f"character id {film_character_id} not found")

                print("Related planets")
                for film_planet in film_planets:
                    film_planet_id = film_planet \
                        .lstrip("https://swapi.dev/api/planet/") \
                        .rstrip('/')

                    try:
                        print(f"planet id {film_planet_id}")
                        _planet = Planet.objects.get(
                            pk=film_planet_id)
                        film.planets.add(_planet)
                    except:
                        print(f"planet id {film_planet_id} not found")

            print("Finished saving films")
        except:
            traceback.print_exc()
