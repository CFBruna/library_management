import pytest
from django.contrib.auth.models import Permission, User
from django.contrib.contenttypes.models import ContentType

from .models import Patron


@pytest.fixture
def patron_fixture():
    return Patron.objects.create(
        name="João da Silva",
        phone_number="11987654321",
        email="joao.silva@example.com",
        cpf="11122233344",
    )


@pytest.fixture
def authenticated_client_for_patrons():
    from django.test import Client

    client = Client()
    user = User.objects.create_user(username="patronstester", password="password123")
    content_type = ContentType.objects.get_for_model(Patron)
    permissions = Permission.objects.filter(content_type=content_type)
    user.user_permissions.set(permissions)
    client.login(username="patronstester", password="password123")
    return client
