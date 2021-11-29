from django.http.response import HttpResponse
from  rest_framework import serializers 
from rest_framework.response import Response
from .models import Books

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['title', 'author', 'language']