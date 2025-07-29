import pytest
from django.urls import reverse

from .models import Author


@pytest.mark.django_db
def test_author_str_representation():
    author = Author.objects.create(name="George Orwell", description="Autor de 1984.")
    assert str(author) == "George Orwell"


@pytest.mark.django_db
def test_author_list_view(authenticated_client_for_authors):
    Author.objects.create(name="J.R.R. Tolkien")
    url = reverse("authors:list")
    response = authenticated_client_for_authors.get(url)
    assert response.status_code == 200
    assert "J.R.R. Tolkien" in response.content.decode("utf-8")
    assert response.templates[0].name == "authors/author_list.html"


@pytest.mark.django_db
def test_author_detail_view(authenticated_client_for_authors):
    author = Author.objects.create(name="Machado de Assis")
    url = reverse("authors:detail", kwargs={"pk": author.pk})
    response = authenticated_client_for_authors.get(url)
    assert response.status_code == 200
    assert "Machado de Assis" in response.content.decode("utf-8")


@pytest.mark.django_db
def test_author_create_view_post(authenticated_client_for_authors):
    url = reverse("authors:create")
    form_data = {"name": "Clarice Lispector", "description": "Escritora e jornalista."}
    response = authenticated_client_for_authors.post(url, data=form_data)
    assert response.status_code == 302
    assert Author.objects.filter(name="Clarice Lispector").exists()


@pytest.mark.django_db
def test_author_update_view_post(authenticated_client_for_authors):
    author = Author.objects.create(name="Graciliano R.")
    url = reverse("authors:update", kwargs={"pk": author.pk})
    form_data = {"name": "Graciliano Ramos", "description": "Autor de Vidas Secas."}
    response = authenticated_client_for_authors.post(url, data=form_data)
    assert response.status_code == 302
    author.refresh_from_db()
    assert author.name == "Graciliano Ramos"


@pytest.mark.django_db
def test_author_delete_view_post(authenticated_client_for_authors):
    author = Author.objects.create(name="Autor a ser apagado")
    url = reverse("authors:delete", kwargs={"pk": author.pk})
    response = authenticated_client_for_authors.post(url)
    assert response.status_code == 302
    assert not Author.objects.filter(pk=author.pk).exists()
