from django.urls import path
from . import views



urlpatterns = [
path("", views.check, name='check'),
path("<int:pk>", views.flashcards, name='flashcards'),
]