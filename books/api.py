from rest_framework import viewsets, permissions, generics
from .models import Books
from .filters import BooksFilter
from .serializers import BooksSerializer
from django_filters import rest_framework as rest_filters


class ViewBooksFilter(BooksFilter):
    title = rest_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Books
        fields = "__all__"

class BooksViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    filterset_class = BooksFilter


