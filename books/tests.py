import pytest
from django.urls import reverse

from .models import Book


@pytest.mark.django_db
def test_book_str_representation(book_fixture):
    expected_string = "O Hobbit (ISBN: 978-0345339683)"
    result_string = str(book_fixture)
    assert result_string == expected_string


@pytest.mark.django_db
def test_book_list_view(authenticated_client, category_fixture):
    Book.objects.create(
        title="1984", category=category_fixture, page_count=328, isbn="123", quantity=1
    )
    url = reverse("books:list")
    response = authenticated_client.get(url)
    assert response.status_code == 200
    assert "1984" in response.content.decode("utf-8")
    assert response.templates[0].name == "books/book_list.html"


@pytest.mark.django_db
def test_book_search_functionality(authenticated_client, category_fixture):
    Book.objects.create(
        title="1984", category=category_fixture, page_count=328, isbn="123", quantity=1
    )
    Book.objects.create(
        title="Fahrenheit 451",
        category=category_fixture,
        page_count=256,
        isbn="456",
        quantity=1,
    )
    base_url = reverse("books:list")
    search_url = f"{base_url}?q=1984"
    response = authenticated_client.get(search_url)
    assert response.status_code == 200
    assert "1984" in response.content.decode("utf-8")
    assert "Fahrenheit 451" not in response.content.decode("utf-8")


@pytest.mark.django_db
def test_book_detail_view(authenticated_client, book_fixture):
    url = reverse("books:detail", kwargs={"pk": book_fixture.pk})
    response = authenticated_client.get(url)
    assert response.status_code == 200
    assert book_fixture.title in response.content.decode("utf-8")


@pytest.mark.django_db
def test_book_create_view_post(authenticated_client, author_fixture, category_fixture):
    url = reverse("books:create")
    form_data = {
        "title": "Revolução dos Bichos",
        "author": author_fixture.pk,
        "category": category_fixture.pk,
        "page_count": 152,
        "isbn": "978-8535902788",
        "quantity": 3,
    }
    response = authenticated_client.post(url, data=form_data)
    assert response.status_code == 302
    assert Book.objects.filter(title="Revolução dos Bichos").exists()


@pytest.mark.django_db
def test_book_update_view_post(
    authenticated_client, book_fixture, author_fixture, category_fixture
):
    url = reverse("books:update", kwargs={"pk": book_fixture.pk})
    novo_titulo = "O Hobbit (Edição Revisada)"
    form_data = {
        "title": novo_titulo,
        "author": author_fixture.pk,
        "category": category_fixture.pk,
        "page_count": book_fixture.page_count,
        "isbn": book_fixture.isbn,
        "quantity": book_fixture.quantity,
    }
    response = authenticated_client.post(url, data=form_data)
    assert response.status_code == 302
    book_fixture.refresh_from_db()
    assert book_fixture.title == novo_titulo


@pytest.mark.django_db
def test_book_delete_view_post(authenticated_client, book_fixture):
    url = reverse("books:delete", kwargs={"pk": book_fixture.pk})
    response = authenticated_client.post(url)
    assert response.status_code == 302
    assert not Book.objects.filter(pk=book_fixture.pk).exists()
