from django.contrib import admin

# Register your models here.
from cards.models import Box, Card


@admin.register(Box)
class BoxAdmin(admin.ModelAdmin):
    list_display = ['id', 'box_name', 'author']

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'answer', 'box']