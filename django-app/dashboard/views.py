from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CategorySerializer, PhraseSerializer
from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Phrase
from .forms import PhraseForm
from django.http import Http404

def home(request):
    return render(request, 'home.html')

class CategoryListView(APIView):
    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PhraseListView(APIView):
    def get(self, request, category_id):
        try:
            category = Category.objects.get(id=category_id)
            Phrase.objects.filter(category=category)
            phrase = category.Phrase.first()
            if phrase:
                serializer = PhraseSerializer(phrase)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"detail": "No phrases found for this category"}, status=status.HTTP_404_NOT_FOUND)
        except Category.DoesNotExist:
            return Response({"detail": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
    
# def phrase_list(request, category_id):
#     category = Category.objects.get(id=category_id)
#     phrases = Phrase.objects.filter(category=category)
#     return render(request, 'dashboard/phrase_list.html', {'category': category, 'phrases': phrases})


from rest_framework import serializers

class PhraseCreateView(APIView):
    def post(self, request):
        serializer = PhraseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
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

# category_id
def create_phrase(request):
    # category = get_object_or_404(Category, id=category_id)  

    if request.method == 'POST':
        form = PhraseForm(request.POST)

        if form.is_valid():
            phrase = form.save(commit=False)
            # phrase.category = category  
            phrase.save()

            return redirect('create_phrase.html')     
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

    return redirect('phrase_list', category_id=liked_category.id)

def delete_phrase(request, phrase_id):
    phrase = get_object_or_404(Phrase, id=phrase_id)

    phrase.delete()

    return redirect('phrase_list', category_id=phrase.category.id)

