from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

import api.models as models
import api.serializers as serializers


class CharactersViewSet(ModelViewSet):
    serializer_class = serializers.CharactersSerializer
    permission_classes = [IsAuthenticated]
    queryset = models.Character.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']


class FilmsViewSet(ModelViewSet):
    serializer_class = serializers.FilmsSerializer
    permission_classes = [IsAuthenticated]
    queryset = models.Film.objects.all()


class PlanetsViewSet(ModelViewSet):
    serializer_class = serializers.PlanetsSerializer
    permission_classes = [IsAuthenticated]
    queryset = models.Planet.objects.all()
