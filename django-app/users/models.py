from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass  

class Struggle(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
