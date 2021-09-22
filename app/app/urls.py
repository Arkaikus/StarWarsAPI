"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from django.conf import settings
from django.conf.urls import url
from django.urls.conf import include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from api.views import *
from rest_framework.routers import DefaultRouter

schema_view = get_schema_view(
    openapi.Info(
        title="StarWars API",
        default_version='v1.0',
        description="Simple API to manage star wars characters and movies",
        terms_of_service="#",
        contact=openapi.Contact(
            email="giraldo.santiago@correounivalle.edu.co"),
        license=openapi.License(name="MIT License"),
    ),
    url=settings.API_URL,
    public=True,
)

router = DefaultRouter()
router.register(r'characters', CharactersViewSet, basename='character')
router.register(r'films', FilmsViewSet, basename='film')
router.register(r'planets', PlanetsViewSet, basename='planet')

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/signup/', include('dj_rest_auth.registration.urls')),
    path('', include(router.urls)),

    # API DOCUMENTATION
    path('doc', schema_view.with_ui(
        'swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0), name='schema-json'),
]
