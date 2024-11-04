from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blueprint_A/', views.blueprint_A, name='blueprint_A'),  
    path('categories/', views.category_list, name='category_list'),
    path('phrases/<int:category_id>/', views.phrase_list, name='phrase_list'),
    path('create_phrase/', views.create_phrase, name='create_phrase'),
]
