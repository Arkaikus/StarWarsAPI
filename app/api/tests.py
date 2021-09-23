from faker import Faker
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import Character, Planet, Film
from django.contrib.auth.models import User

# Create your tests here.


class AccountTests(APITestCase):
    def test_create_account(self):
        """
            Ensure we can create a new account object.
        """        
        data = {
            "username": "root",
            "email": "root@api.com",
            "password1": "o2w59H@5#u",
            "password2": "o2w59H@5#u",
        }

        response = self.client.post("/auth/signup/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, "root")


class CharacterTests(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username="root", password="o2w59H@5#u")
        return super().setUp()

    def test_create_character(self):        
        data = {
            "name": "Luke Skywalker",
        }
        self.client.force_login(self.user)
        response = self.client.post("/characters/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Character.objects.count(), 1)
        self.assertEqual(Character.objects.get().name, "Luke Skywalker")

    def test_modify_character(self):
        luke = Character(name="Luke Skywalker")
        luke.save()
        self.assertEqual(Character.objects.count(), 1)

        data = {
            "name": "Luke Skywalker Renamed",
            "films":[]
        }
        self.client.force_login(self.user)
        response = self.client.put(f"/characters/{luke.id}/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Character.objects.get().name, "Luke Skywalker Renamed")

    def test_delete_character(self):
        luke = Character(name="Luke Skywalker")
        luke.save()
        self.assertEqual(Character.objects.count(), 1)

        self.client.force_login(self.user)
        response = self.client.delete(f"/characters/{luke.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Character.objects.count(), 0)

class FilmTests(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username="root", password="o2w59H@5#u")
        return super().setUp()

    def test_create_film(self):        
        data = {
            "title": "A New Hope",
            "prelude": "Story"            
        }
        self.client.force_login(self.user)
        response = self.client.post("/films/", data)        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Film.objects.count(), 1)
        self.assertEqual(Film.objects.get().title, "A New Hope")

    def test_modify_film(self):
        film = Film(title="A New Hope", prelude="Story")
        film.save()
        self.assertEqual(Film.objects.count(), 1)

        data = {
            "title": "A New Hope Renamed",
            "prelude": "Story revamped",
        }
        self.client.force_login(self.user)
        response = self.client.put(f"/films/{film.id}/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Film.objects.get().title, "A New Hope Renamed")
        self.assertEqual(Film.objects.get().prelude, "Story revamped")

    def test_delete_film(self):
        film = Film(title="A New Hope")
        film.save()
        self.assertEqual(Film.objects.count(), 1)

        self.client.force_login(self.user)
        response = self.client.delete(f"/films/{film.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Film.objects.count(), 0)

class PlanetTests(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username="root", password="o2w59H@5#u")
        return super().setUp()

    def test_create_planet(self):        
        data = {
            "name": "Tatooine",
        }
        self.client.force_login(self.user)
        response = self.client.post("/planets/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Planet.objects.count(), 1)
        self.assertEqual(Planet.objects.get().name, "Tatooine")

    def test_modify_planet(self):
        planet = Planet(name="Tatooine")
        planet.save()
        self.assertEqual(Planet.objects.count(), 1)

        data = {
            "name": "Tatooine Renamed",
            "films":[]
        }
        self.client.force_login(self.user)
        response = self.client.put(f"/planets/{planet.id}/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Planet.objects.get().name, "Tatooine Renamed")

    def test_delete_planet(self):
        planet = Planet(name="Tatooine")
        planet.save()
        self.assertEqual(Planet.objects.count(), 1)

        self.client.force_login(self.user)
        response = self.client.delete(f"/planets/{planet.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Planet.objects.count(), 0)