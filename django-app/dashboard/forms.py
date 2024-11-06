from django import forms
from .models import Phrase, Category

class PhraseForm(forms.ModelForm):

    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Selecione uma Categoria", widget=forms.Select())

    class Meta:
        model = Phrase
        fields = ['author', 'content', 'category']
