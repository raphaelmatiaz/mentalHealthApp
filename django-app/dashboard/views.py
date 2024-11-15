from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Phrase
from .forms import PhraseForm
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, 'home.html')

def phrase_list(request, category_id):
    category = Category.objects.get(id=category_id)
    phrases = Phrase.objects.filter(category=category)
    return render(request, 'dashboard/phrase_list.html', {'category': category, 'phrases': phrases})

def category_list(request):
    categories = Category.objects.all()

    return render(request, 'dashboard/category_list.html', {'categories': categories})

def create_phrase(request):

    if request.method == 'POST':
        form = PhraseForm(request.POST)

        if form.is_valid():
            phrase = form.save(commit=False)
            phrase.save()

            form = PhraseForm()

            return render(request, 'dashboard/create_phrase.html', {'form': form})    
    else:
        form = PhraseForm()

    return render(request, 'dashboard/create_phrase.html', {'form': form})


def delete_phrase(request, phrase_id):
    phrase = get_object_or_404(Phrase, id=phrase_id)

    phrase.delete()
