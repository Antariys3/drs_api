import time

from django.core.cache import cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import viewsets
from rest_framework.response import Response

from book.models import Book, Author
from book.serializers import BookSerializer, AuthorSerializer


class BookListView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @method_decorator(cache_page(60 * 5))
    def list(self, request, *args, **kwargs):
        time.sleep(3)
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):  # method to delete cache if database has changed
        response = super().create(request, *args, **kwargs)
        cache.clear()
        return response


class AuthorListView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    @method_decorator(cache_page(60 * 5))
    def list(self, request, *args, **kwargs):
        time.sleep(3)
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):  # method to delete cache if database has changed
        response = super().create(request, *args, **kwargs)
        cache.clear()
        return response
