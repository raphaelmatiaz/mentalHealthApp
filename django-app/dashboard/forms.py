from django import forms
from .models import Phrase

class PhraseForm(forms.ModelForm):
    class Meta:
        model = Phrase
        fields = ['author', 'content', 'category']
