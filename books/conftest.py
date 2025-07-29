import pytest
from django.contrib.auth.models import Permission, User
from django.contrib.contenttypes.models import ContentType

from authors.models import Author
from categories.models import Category

from .models import Book


@pytest.fixture
def author_fixture():
    return Author.objects.create(name="J.R.R. Tolkien")


@pytest.fixture
def category_fixture():
    return Category.objects.create(name="Fantasia")


@pytest.fixture
def book_fixture(author_fixture, category_fixture):
    book = Book.objects.create(
        title="O Hobbit",
        category=category_fixture,
        page_count=300,
        isbn="978-0345339683",
        quantity=5,
    )
    book.author.add(author_fixture)
    return book


@pytest.fixture
def authenticated_client():
    from django.test import Client

    client = Client()
    user = User.objects.create_user(username="testuser", password="password123")
    content_type = ContentType.objects.get_for_model(Book)
    permissions = Permission.objects.filter(content_type=content_type)
    user.user_permissions.set(permissions)
    client.login(username="testuser", password="password123")
    return client
