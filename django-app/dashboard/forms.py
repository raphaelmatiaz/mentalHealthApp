from django import forms
from .models import Phrase, Category

class PhraseForm(forms.ModelForm):
    class Meta:
        model = Phrase
        fields = ['content', 'category']
