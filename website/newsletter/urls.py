from django.urls import path
from .views import suscribe


urlpatterns = [
    path('',suscribe, name='newsletter'),
]
