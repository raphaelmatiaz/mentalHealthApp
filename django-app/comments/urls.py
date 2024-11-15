from comments.views import get_comments
from django.urls import path
from . import views


urlpatterns = [
    # path("<int:category_id>/", get_comments, name="comments"),
    path('comments/', views.get_comments, name='get_comments'),
    path('comments/', views.view_post_comment, name='post_comments'),  
]
