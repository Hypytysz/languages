from django import forms

from cards.models import Card, Box


class BoxForm(forms.ModelForm):
    class Meta:
        model = Box
        fields = ['box_name']


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['question', 'answer', 'box']