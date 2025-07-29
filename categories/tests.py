import pytest
from django.urls import reverse

from .models import Category


@pytest.mark.django_db
def test_category_str_representation():
    category = Category.objects.create(name="Ficção Científica")
    assert str(category) == "Ficção Científica"


@pytest.mark.django_db
def test_category_list_view(authenticated_client_for_categories):
    Category.objects.create(name="Fantasia")
    url = reverse("categories:list")
    response = authenticated_client_for_categories.get(url)
    assert response.status_code == 200
    assert "Fantasia" in response.content.decode("utf-8")
    assert response.templates[0].name == "categories/category_list.html"


@pytest.mark.django_db
def test_category_detail_view(authenticated_client_for_categories):
    category = Category.objects.create(name="Romance")
    url = reverse("categories:detail", kwargs={"pk": category.pk})
    response = authenticated_client_for_categories.get(url)
    assert response.status_code == 200
    assert "Romance" in response.content.decode("utf-8")


@pytest.mark.django_db
def test_category_create_view_post(authenticated_client_for_categories):
    url = reverse("categories:create")
    form_data = {
        "name": "Aventura",
        "description": "Livros com muita ação e exploração.",
    }
    response = authenticated_client_for_categories.post(url, data=form_data)
    assert response.status_code == 302
    assert Category.objects.filter(name="Aventura").exists()


@pytest.mark.django_db
def test_category_update_view_post(authenticated_client_for_categories):
    category = Category.objects.create(name="Mistério")
    url = reverse("categories:update", kwargs={"pk": category.pk})
    form_data = {
        "name": "Suspense e Mistério",
        "description": "Livros que prendem a atenção.",
    }
    response = authenticated_client_for_categories.post(url, data=form_data)
    assert response.status_code == 302
    category.refresh_from_db()
    assert category.name == "Suspense e Mistério"


@pytest.mark.django_db
def test_category_delete_view_post(authenticated_client_for_categories):
    category = Category.objects.create(name="Categoria a ser apagada")
    url = reverse("categories:delete", kwargs={"pk": category.pk})
    response = authenticated_client_for_categories.post(url)
    assert response.status_code == 302
    assert not Category.objects.filter(pk=category.pk).exists()
