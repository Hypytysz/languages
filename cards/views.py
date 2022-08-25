from django.shortcuts import render, redirect

# Create your views here.
from cards.forms import BoxForm, CardForm
from cards.models import Card, Box


def card_list(request):
    card_list = Card.objects.all().order_by("box", "-date_created")
    return render(request, 'cards/card_list.html', {'card_list': card_list})

def new_box(request):
    if request.method == "POST":
        form = BoxForm(data=request.POST)
        if form.is_valid():
            box = form.save(commit=False)
            box.author = request.user
            box.save()
    return render(request, 'cards/new_box.html', {'form': BoxForm()})

def box_delete(request, pk):
    Box.objects.filter(id=pk).delete()
    return redirect('card_list')

def new_card(request):
    if request.method == "POST":
        form = CardForm(data=request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            card.author = request.user
            card.save()
    return render(request, 'cards/new_card.html', {'form': CardForm()})

def card_edit(request, pk):
    card = Card.objects.get(pk=pk)
    data = {'question':card.question, 'answer':card.answer, 'box':card.box}
    edit_form = CardForm(data=data)
    if request.method == "POST":
        edit_form = CardForm(request.POST, instance=card)
        if edit_form.is_valid():
            card.question = edit_form.cleaned_data['question']
            card.answer = edit_form.cleaned_data['answer']
            card.box = edit_form.cleaned_data['box']
            card.save()
            return redirect("card_list")
    return render(request, 'cards/edit.html', {"card":card, 'edit_form': edit_form})


def card_details(request, pk):
    details = Card.objects.get(pk=pk)
    card = Card.objects.filter(pk=pk).first().box_id
    card_list = Card.objects.filter(box=card)
    return render(request, 'cards/card.html', {"card":details, 'card_list':card_list})

def card_delete(request, pk):
    card = Card.objects.filter(pk=pk).first().box_id
    Card.objects.filter(id=pk).delete()
    box = Card.objects.filter(box=card).first().id
    return redirect('card', pk=box)

def answer(request, pk):
    details = Card.objects.get(pk=pk)
    card = Card.objects.filter(pk=pk).first().box_id
    card_list = Card.objects.filter(box=card)
    return render(request, 'cards/answer.html', {"card":details, 'card_list':card_list})