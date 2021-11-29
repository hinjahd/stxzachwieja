from typing import OrderedDict
from django.db.models import query
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.response import Response

from books.serializers import BooksSerializer
from .models import Books
from .filters import BooksFilter
from .forms import booksForm
from django.core import serializers
import requests
import pprint
from rest_framework.filters import SearchFilter
import django_filters.rest_framework
from rest_framework import generics
    




def main(request):

    books_data = Books.objects.all()

    filter = BooksFilter(request.GET, queryset=books_data)
    books_data = filter.qs


    context = {
        'book' : books_data,
        'filter':filter,
    }
    return render(request, 'books/index.html', context)


def createBook(request):

    form = booksForm()

    if request.method == "POST":
        form = booksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {

        'form':form

    }
    return render(request, 'books/create.html', context)


def updateBook(request, pk):
    book = Books. objects.get(id = pk)
    form = booksForm(instance = book)

    if request.method == "POST":
        form = booksForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form':form
    }
    return render(request, 'books/create.html', context)

def deleteBook(request, pk):

    book = Books.objects.get(id=pk)

    if request.method == "POST":
        book.delete()
        return redirect('/')

    context = {'book':book}

    return render(request, 'books/delete.html', context)


def search(request):

    if request.method == "POST":

        Object = {
            'name': request.POST['name']
        }

        searched_book = Object['name']

        url2 = 'https://www.googleapis.com/books/v1/volumes?q='+searched_book
        r = requests.get(url2)
        titles = r.json()

        books_list = []
 

    

        for title in titles['items']:
            try:
                book_dict = {
                    
                    'title': title['volumeInfo']['title'],
                    'image_link': title['volumeInfo']['imageLinks']['thumbnail'] if 'imageLinks' in title['volumeInfo'] else "img src",
                    'author': ", ".join(title['volumeInfo']['authors']) if 'authors' in title['volumeInfo'] else "defualt author",
                    'ISBN': (title['volumeInfo']['industryIdentifiers'][0]['identifier']) if 'identifier' in title['volumeInfo']['industryIdentifiers'][0] else "???",
                    'pub_date': title['volumeInfo']['publishedDate'],
                    'language': title['volumeInfo']['language'],
                    'num_of_pages' : title['volumeInfo']['pageCount'] if "pageCount" in title['volumeInfo'] else 1,
                }
                
            except:
                pprint.pprint(books_list)
                pass

            books_list.append(book_dict)
            
        

        #pprint.pprint(books_list)

        for item in books_list:
            c = Books.objects.get_or_create(**item)

        return redirect('/')

    return render(request, 'books/search.html')
