from django.urls import path, include
from . import views



urlpatterns = [
    # URLs tradicionais do app
    path('', views.home, name='home'),
    path('create-phrase/<int:category_id>/', views.create_phrase, name='create_phrase'),  
    path('categories/', views.category_list, name='category_list'),  
    path('phrases/<int:category_id>/', views.phrase_list, name='phrase_list'),  
]

