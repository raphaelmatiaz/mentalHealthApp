from rest_framework import serializers
from .models import Category, Phrase

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'nome']

class PhraseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phrase
        fields = ['id', 'author', 'content', 'created_at', 'categoria']