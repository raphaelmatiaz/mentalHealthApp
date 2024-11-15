from django.urls import path, include
from . import views



urlpatterns = [
    # URLs tradicionais do app
    path('', views.home, name='home'),
    path('create-phrase/', views.create_phrase, name='create_phrase'),  
    path('categories/', views.category_list, name='category_list'),  
    path('phrases/<int:category_id>/', views.phrase_list, name='phrase_list'),  
    path('phrases/<int:category_id>/comments/', views.view_get_phrase_comments, name='get_phrase_comments'),
    path('phrases/<int:category_id>/comments/add/', views.view_post_comment, name='add_comment'),
    # path('like/<int:phrase_id>/', views.like_phrase, name='like_phrase'),
    # path('delete/<int:phrase_id>/', views.delete_phrase, name='delete_phrase'),
]

