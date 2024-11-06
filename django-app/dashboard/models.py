from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    @classmethod
    def get_or_create_liked_category(cls):
        # Tenta encontrar ou criar a categoria "Frases Curtidas"
        category, created = cls.objects.get_or_create(name="Frases Curtidas")
        return category

    def __str__(self):
        return self.name

class Phrase(models.Model):
    content = models.TextField()
    author = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content