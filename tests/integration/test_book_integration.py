from datetime import date

import requests

SERVER_URL = "http://127.0.0.1:8000/"


def test_get_api_author():
    r = requests.get(SERVER_URL + "authors/")
    r.raise_for_status()
    assert r.status_code == 200
    r = requests.get(SERVER_URL + "authors/1/")
    assert r.json() == {"id": 1, "name": "Владимир Сушкин"}


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
    r = requests.get(SERVER_URL + "books/1/")
    assert r.json() == {
        "id": 1,
        "title": "Лиат душа Эсхейма",
        "genre": "Приключения",
        "time_create": "2023-12-18",
        "author": 1,
    }


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
