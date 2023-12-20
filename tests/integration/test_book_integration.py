from datetime import date

import requests

SERVER_URL = "https://infinite-retreat-84129-fa7490995c53.herokuapp.com/"


def test_get_api_author():
    r = requests.get(SERVER_URL + "authors/")
    r.raise_for_status()
    assert r.status_code == 200


def test_create_author():
    r = requests.post(SERVER_URL + "authors/", json={"name": "Стефені Маєр"})
    r.raise_for_status()
    assert r.status_code == 201
    assert r.json()["name"] == "Стефені Маєр"


def test_create_author_with_error():
    r = requests.post(SERVER_URL + "authors/", json={})
    assert r.status_code == 400
    assert "Обязательное поле." in r.json()["name"]


def test_get_api_book():
    r = requests.get(SERVER_URL + "books/")
    r.raise_for_status()
    assert r.status_code == 200


def test_create_book():
    r = requests.post(
        SERVER_URL + "books/",
        json={"title": "Затемнення", "genre": "Роман", "time_create": str(date.today()), "author": 1},
    )
    r.raise_for_status()
    assert r.status_code == 201
    assert (r.json()["title"], r.json()["genre"], r.json()["time_create"], r.json()["author"]) == (
        "Затемнення",
        "Роман",
        str(date.today()),
        1,
    )


def test_create_book_with_error():
    r = requests.post(SERVER_URL + "books/", json={})
    assert r.status_code == 400
    assert "Обязательное поле." in r.json()["title"]
