from django.shortcuts import render
import random

# Create your views here.
from levels.forms import AnswerForm


def basic(request):
    f = open(
        "static/txt/a1_a2.txt",
        "r",
        encoding="utf-8",
    )
    zawartosc = f.read()
    zawartosc = zawartosc.split(";")
    zawartosc = random.choice(zawartosc).strip()
    zawartosc = zawartosc.split(',')
    zawartosc1 = zawartosc[0]
    zawartosc2 = zawartosc[1]
    f.close()
    answer = request.POST.get('answer')
    return render(request, 'levels/basic.html', {'basic1':zawartosc1, 'basic2': zawartosc2, 'answer':answer})

def intermediate(request):
    f = open(
        "static/txt/b1_b2.txt",
        "r",
        encoding="utf-8",
    )
    zawartosc = f.read()
    zawartosc = zawartosc.split("|")
    zawartosc = random.choice(zawartosc).strip()
    zawartosc = zawartosc.split(':')
    zawartosc1 = zawartosc[0]
    zawartosc2 = zawartosc[1]
    f.close()
    form = AnswerForm(request.POST)
    return render(request, 'levels/intermediate.html', {'intermediate1': zawartosc1, 'intermediate2': zawartosc2, 'form':form})

def advanced(request):
    f = open(
        "static/txt/c1_c2.txt",
        "r",
        encoding="utf-8",
    )
    zawartosc = f.read()
    zawartosc = zawartosc.split(";")
    zawartosc = random.choice(zawartosc).strip()
    zawartosc = zawartosc.split(',')
    zawartosc1 = zawartosc[0]
    zawartosc2 = zawartosc[1]
    f.close()
    return render(request, 'levels/advanced.html', {'advanced1':zawartosc1, 'advanced2': zawartosc2})

