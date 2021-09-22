from django.db import models

# Create your models here.

class Character(models.Model):
    name = models.CharField(max_length=255)

class Planet(models.Model):
    name = models.CharField(max_length=255)

class Film(models.Model):
    title = models.CharField(max_length=255)
    prelude = models.CharField(max_length=255)
    characters = models.ManyToManyField(Character, related_name='films')
    planets = models.ManyToManyField(Planet, related_name='films')
