from django.shortcuts import render, redirect
from .models import Category, Phrase
from .forms import PhraseForm

def home(request):
    return render(request, 'home.html')

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'dashboard/category_list.html', {'categories': categories})


def phrase_list(request, category_id):
    category = Category.objects.get(id=category_id)
    phrases = Phrase.objects.filter(category=category)
    return render(request, 'dashboard/phrase_list.html', {'category': category, 'phrases': phrases})

def create_phrase(request):
    if request.method == 'POST':
        form = PhraseForm(request.POST)
        if form.is_valid():
            phrase = form.save(commit=False)
            phrase.user = request.user
            phrase.save()
            return redirect('phrase_list', category_id=phrase.category.id)
    else:
        form = PhraseForm()
    return render(request, 'dashboard/create_phrase.html', {'form': form})


def blueprint_A(request):
    return render(request, 'dashboard/blueprint_A.html')  