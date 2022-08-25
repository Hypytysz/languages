from django.shortcuts import render

# Create your views here.
from cards.models import Box, Card


def check(request):
    box_list = Box.objects.all().order_by("id")
    card_list = Card.objects.all()
    return render(request, 'cards/check.html', {'box_list': box_list, 'card_list': card_list})

def flashcards(request, pk):
    box = Box.objects.get(pk=pk)
    boxs = box.boxs.first()
    rest = box.boxs.all()
    return render(request, 'cards/flashcards.html', {"box": box, 'boxs': boxs, 'rest': rest})

