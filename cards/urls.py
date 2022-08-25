from django.urls import path
from . import views



urlpatterns = [

    path('', views.card_list, name='card_list'),
    path('new_box', views.new_box, name='new_box'),
    path('new_card', views.new_card, name='new_card'),
    path("edit/<int:pk>", views.card_edit, name="edit"),
    path("<int:pk>", views.card_details, name='card'),
    path("delete/<int:pk>", views.card_delete, name="delete"),
    path("answer/<int:pk>", views.answer, name='answer'),
    path("box/<int:pk>", views.box_delete, name="box_delete"),
]