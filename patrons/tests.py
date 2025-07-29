import pytest
from django.urls import reverse

from .models import Patron


@pytest.mark.django_db
def test_patron_str_representation(patron_fixture):
    expected_string = "João da Silva (CPF: 11122233344)"
    assert str(patron_fixture) == expected_string


@pytest.mark.django_db
def test_patron_list_view_and_search(authenticated_client_for_patrons, patron_fixture):
    url = reverse("patrons:list")
    response = authenticated_client_for_patrons.get(url)
    assert response.status_code == 200
    assert patron_fixture.name in response.content.decode("utf-8")
    assert response.templates[0].name == "patrons/patron_list.html"
    search_url = f"{url}?q={patron_fixture.cpf}"
    response_search = authenticated_client_for_patrons.get(search_url)
    assert response_search.status_code == 200
    assert patron_fixture.name in response_search.content.decode("utf-8")


@pytest.mark.django_db
def test_patron_detail_view(authenticated_client_for_patrons, patron_fixture):
    url = reverse("patrons:detail", kwargs={"pk": patron_fixture.pk})
    response = authenticated_client_for_patrons.get(url)
    assert response.status_code == 200
    assert patron_fixture.email in response.content.decode("utf-8")


@pytest.mark.django_db
def test_patron_create_view_post(authenticated_client_for_patrons):
    url = reverse("patrons:create")
    form_data = {
        "name": "Maria Oliveira",
        "phone_number": "21912345678",
        "email": "maria.oliveira@example.com",
        "cpf": "55566677788",
    }
    response = authenticated_client_for_patrons.post(url, data=form_data)
    assert response.status_code == 302
    assert Patron.objects.filter(cpf="55566677788").exists()


@pytest.mark.django_db
def test_patron_update_view_post(authenticated_client_for_patrons, patron_fixture):
    url = reverse("patrons:update", kwargs={"pk": patron_fixture.pk})
    novo_email = "joao.silva.novo@example.com"
    form_data = {
        "name": patron_fixture.name,
        "phone_number": patron_fixture.phone_number,
        "email": novo_email,
        "cpf": patron_fixture.cpf,
    }
    response = authenticated_client_for_patrons.post(url, data=form_data)
    assert response.status_code == 302
    patron_fixture.refresh_from_db()
    assert patron_fixture.email == novo_email


@pytest.mark.django_db
def test_patron_delete_view_post(authenticated_client_for_patrons, patron_fixture):
    url = reverse("patrons:delete", kwargs={"pk": patron_fixture.pk})
    patron_pk = patron_fixture.pk
    response = authenticated_client_for_patrons.post(url)
    assert response.status_code == 302
    assert not Patron.objects.filter(pk=patron_pk).exists()
