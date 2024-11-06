from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CategorySerializer, PhraseSerializer
from django.shortcuts import render, redirect
from .models import Category, Phrase
from .forms import PhraseForm

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