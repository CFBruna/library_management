import pytest
from django.contrib.auth.models import Permission, User
from django.contrib.contenttypes.models import ContentType

from authors.models import Author
from books.models import Book
from categories.models import Category
from patrons.models import Patron

from .models import Loan


@pytest.fixture
def author_for_loan_tests():
    return Author.objects.create(name="Autor Teste Empréstimo")


@pytest.fixture
def category_for_loan_tests():
    return Category.objects.create(name="Categoria Teste Empréstimo")


@pytest.fixture
def book_for_loan_tests(author_for_loan_tests, category_for_loan_tests):
    book = Book.objects.create(
        title="Livro para Empréstimo",
        category=category_for_loan_tests,
        page_count=100,
        isbn="1234567890123",
        quantity=5,
    )
    book.author.add(author_for_loan_tests)
    return book


@pytest.fixture
def patron_for_loan_tests():
    return Patron.objects.create(
        name="Leitor Teste",
        phone_number="11999999999",
        email="leitor.teste@example.com",
        cpf="12345678901",
    )


@pytest.fixture
def authenticated_client_for_loans():
    from django.test import Client

    client = Client()
    user = User.objects.create_user(username="loanstester", password="password123")
    content_type = ContentType.objects.get_for_model(Loan)
    permissions = Permission.objects.filter(content_type=content_type)
    user.user_permissions.set(permissions)
    client.login(username="loanstester", password="password123")
    return client
