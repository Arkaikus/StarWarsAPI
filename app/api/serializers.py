from api.models import Character, Film, Planet
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class CharactersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Character
        fields = ('id', 'name', 'films')


class FilmsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Film
        fields = ('id', 'title', 'prelude', 'characters', 'planets')


class PlanetsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Planet
        fields = ('id', 'name', 'films')
