from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Phrase
from .forms import PhraseForm
from django.http import Http404

def home(request):
    return render(request, 'home.html')

def category_list(request): 
    categories = [
        {"id": 1, "name": "Sadness"},
        {"id": 2, "name": "Lack of Confidence"},
        {"id": 3, "name": "Stress at Work"},
        {"id": 4, "name": "Guilt"},
        {"id": 5, "name": "Body Image"},
        {"id": 6, "name": "Social Anxiety"},
        {"id": 7, "name": "Loneliness"},
        {"id": 8, "name": "Self-Doubt"},
        {"id": 9, "name": "Anxiety"},
        {"id": 10, "name": "Anger Management"},
        {"id": 11, "name": "Procrastination"},
        {"id": 12, "name": "Imposter Syndrome"}
    ]
    return render(request, 'dashboard/category_list.html', {'categories': categories})

def phrase_list(request, category_id):
    category = get_object_or_404(Category, id=category_id) 
    phrases = Phrase.objects.filter(category=category)  
    return render(request, 'dashboard/phrase_list.html', {
        'category': category,
        'phrases': phrases
    })

def create_phrase(request, category_id):
    category = get_object_or_404(Category, id=category_id)  

    if request.method == 'POST':
        form = PhraseForm(request.POST)
        if form.is_valid():
            phrase = form.save(commit=False)
            phrase.category = category  
            phrase.save()
            return redirect('phrase_list', category_id=phrase.category_id)     
    else:
        form = PhraseForm()

    return render(request, 'dashboard/create_phrase.html', {'form': form, 'category': category})

def like_phrase(request, phrase_id):
    phrase = get_object_or_404(Phrase, id=phrase_id)

    liked_category, created = Category.objects.get_or_create(name="Frases Curtidas")

    phrase.category = liked_category
    phrase.save()

    return redirect('phrase_list', category_id=liked_category.id)

def delete_phrase(request, phrase_id):
    phrase = get_object_or_404(Phrase, id=phrase_id)

    phrase.delete()

    return redirect('phrase_list', category_id=phrase.category.id)

