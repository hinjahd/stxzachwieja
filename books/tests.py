from django.test import TestCase
from .models import Books
from django.test import Client
from django.urls import reverse
from .forms import booksForm

# Create your tests here.


class URLtests(TestCase):

    def test_testhomepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_testcreate(self):
        response = self.client.get('/create')
        self.assertEqual(response.status_code, 200)

    def test_testsearch(self):
        response = self.client.get('/search')
        self.assertEqual(response.status_code, 200)

        

class BooksTests(TestCase):
    def setUp(self):
        book_a = Books(title = "test1", author = "author1")
        book_a.pub_date = "2019"
        book_a.ISBN = "34234324235"
        book_a.num_of_pages = 3
        book_a.image_link="none"
        book_a.language = "sp"
        book_a.save()
        


    def test_bookexists(self):
        book_count = Books.objects.all().count()
        self.assertEqual(book_count, 1)
        self.assertNotEqual(book_count, 0)

class PageTests(TestCase):
    def setUp(self):
        self.client = Client()
        book_a = Books(title = "test1", author = "author1")
        book_a.pub_date = "2019"
        book_a.ISBN = "34234324235"
        book_a.num_of_pages = 3
        book_a.image_link="none"
        book_a.language = "sp"
        book_a.save()

        
    def test_index(self):
        url = reverse('main')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/index.html')
        self.assertContains(response, 'test1')

    def test_search(self):
        url = reverse('search')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/search.html')
        self.assertContains(response, '')

class AddBookFormTests(TestCase):
    def test_title_starting_lowercase(self):
        form = booksForm(data={"title": "a lowercase title"})

        self.assertEqual(
            form.errors["title"], ["Should start with an uppercase letter"]
        )

    def test_title_ending_full_stop(self):
        form = booksForm(data={"title": "A stopped title."})

        self.assertEqual(form.errors["title"], ["Should not end with a full stop"])

    def test_title_with_ampersand(self):
        form = booksForm(data={"title": "Dombey & Son"})

        self.assertEqual(form.errors["title"], ["Use 'and' instead of '&'"])


        



    