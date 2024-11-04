from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Phrase(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)  
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content


