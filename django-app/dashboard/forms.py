from django import forms
from .models import Phrase, Category
from mongo.models import PhraseComments

class PhraseForm(forms.ModelForm):

    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Selecione uma Categoria", widget=forms.Select())

    class Meta:
        model = Phrase
        fields = ['author', 'content', 'category']


class CommentForm(forms.Form):
    content = forms.CharField(label='Comment', widget=forms.Textarea)
    author = forms.CharField(label='Author', max_length=100)
    category = forms.CharField(label='Category', max_length=100)

