import json
from datetime import date

import pytest
from django.test import Client
from rest_framework import status

from book.models import Author, Book


@pytest.fixture
def client():
    return Client()


@pytest.mark.django_db
def test_author_list_view(client):
    Author.objects.create(name="Test Author")
    response = client.get("/authors/")
    assert response.status_code == status.HTTP_200_OK
    expected_data = [{"id": 1, "name": "Test Author"}]
    assert response.data == expected_data
    assert Author.objects.count() == len(expected_data)


@pytest.mark.django_db
def test_book_list_view(client):
    author = Author.objects.create(name="Test Author")
    Book.objects.create(title="Test book", author=author, genre="Test genre")
    response = client.get("/books/")
    assert response.status_code == status.HTTP_200_OK
    expected_data = [
        {
            "id": 1,
            "title": "Test book",
            "genre": "Test genre",
            "time_create": str(date.today()),
            "author": author.id,
        },
    ]
    print(response.data)
    print(expected_data)
    assert json.loads(json.dumps(response.data)) == expected_data
    assert Book.objects.count() == len(expected_data)
