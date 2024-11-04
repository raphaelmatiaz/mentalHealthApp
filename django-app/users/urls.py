from django.urls import path
from . import views
from .views import SignupView, LoginView, LogoutView

urlpatterns = [
    path('signup/', SignupView, name='signup'),
    path('login/', LoginView, name='login'),  
    path('logout/', LogoutView, name='logout'),
]
