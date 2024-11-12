from ctypes import create_string_buffer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CategorySerializer, PhraseSerializer
from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Phrase
from .forms import PhraseForm
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, 'home.html')

def frontendbuild(request):
    return render(request, 'phrase_list.html')

def phrase_list(request, category_id):
    category = Category.objects.get(id=category_id)
    phrases = Phrase.objects.filter(category=category)
    return render(request, 'dashboard/phrase_list.html', {'category': category, 'phrases': phrases})

def category_list(request):
    categories = Category.objects.all()

    return render(request, 'dashboard/category_list.html', {'categories': categories})

@csrf_exempt
def create_phrase(request):
    # category = get_object_or_404(Category, id=category_id)  

    if request.method == 'POST':
        form = PhraseForm(request.POST)

        if form.is_valid():
            phrase = form.save(commit=False)
            # phrase.category = category  
            phrase.save()

            form = PhraseForm()

            return render(request, 'dashboard/create_phrase.html', {'form': form})    
    else:
        form = PhraseForm()

    return render(request, 'dashboard/create_phrase.html', {'form': form})


def select_category(request):
    categories = [
        {"name": "Sadness"},
        {"name": "Lack of Confidence"},
        {"name": "Stress at Work"},
        {"name": "Guilt"},
        {"name": "Body Image"},
        {"name": "Social Anxiety"},
        {"name": "Loneliness"},
        {"name": "Self-Doubt"},
        {"name": "Anxiety"},
        {"name": "Anger Management"},
        {"name": "Procrastination"},
        {"name": "Imposter Syndrome"}
    ]
    return render(request, 'selectrable_buttons.html', {'categories': categories})

    return render(request, 'dashboard/create_phrase.html', {'form': form, 'category': category})

def like_phrase(request, phrase_id):
    phrase = get_object_or_404(Phrase, id=phrase_id)

    liked_category, created = Category.objects.get_or_create(name="Frases Curtidas")

    phrase.category = liked_category
    phrase.save()

    # return redirect('phrase_list', category_id=liked_category.id)

def delete_phrase(request, phrase_id):
    phrase = get_object_or_404(Phrase, id=phrase_id)

    phrase.delete()

    # return redirect('phrase_list', category_id=phrase.category.id)

