from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Phrase
from .forms import CommentForm, PhraseForm
from django.http import Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from mongo.models import CategoryComments, Comment
from mongo.mongo import Mongo
from django.views.decorators.http import require_http_methods
import json
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR
from rest_framework.request import Request


#Postgres
def home(request):
    return render(request, 'dashboard/home.html')

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

# MongoDB
mongo = Mongo()


def view_get_phrase_comments(request: Request, category_id):
    comments=mongo.db_get_comment(category_id)
        
    if not comments:
        return JsonResponse(
            data={"error": "Commments not found"}, 
            status=HTTP_404_NOT_FOUND
        )
    
    serializer = CategoryComments(root=comments)
    return JsonResponse(
        data={"comments": serializer.model_dump()}, 
        status=HTTP_200_OK
    )


def view_post_comment(request: Request, category_id):      
    
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():

            author = form.cleaned_data['author']
            content = form.cleaned_data['content']
            
            successfull = mongo.db_add_comment(
                author=author,
                category_id=category_id,
                content=content
            )
            
            if successfull:
                return JsonResponse(
                    data={"message": "Comment added successfully"},
                    status=HTTP_200_OK
                )
            else:
                return JsonResponse(
                    data={"error": "Failed to add comment"},
                    status=HTTP_500_INTERNAL_SERVER_ERROR
                )
            
            form = CommentForm()

            return render(request, 'dashboard/create_phrase.html', {'form': form})    
    else:
        form = CommentForm()
    
    return render(request, 'dashboard/create_phrase.html', {'form': form})    

