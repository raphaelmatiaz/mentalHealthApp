from comments.views import get_comments
from django.urls import path
from . import views


urlpatterns = [
    # path("<int:category_id>/", get_comments, name="comments"),
    path('comments/', views.get_comments, name='get_comments'),
    path('comments/', views.post_comment, name='post_comments'),  
    path('comments/delete/<str:comment_id>/', views.delete_comment, name='delete_comments'), 
    path('comments/', views.comment_list, name='comment_list'),  
]
