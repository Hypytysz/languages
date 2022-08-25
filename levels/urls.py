from django.urls import path
from . import views



urlpatterns = [

    path('basic/', views.basic, name='basic'),
    path('intermediate/', views.intermediate, name='intermediate'),
    path('advanced/', views.advanced, name='advanced'),
]