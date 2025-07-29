from datetime import timedelta

import pytest
from django.urls import reverse
from django.utils import timezone

from .forms import LoanForm
from .models import Loan


@pytest.mark.django_db
def test_loan_str_representation(book_for_loan_tests, patron_for_loan_tests):
    loan = Loan.objects.create(
        book=book_for_loan_tests, patron=patron_for_loan_tests, due_date=timezone.now()
    )
    expected_str = f'Empréstimo de "{book_for_loan_tests}" para {
        patron_for_loan_tests.name
    } em {loan.loan_date.strftime("%d/%m/%Y")}'
    assert str(loan) == expected_str


@pytest.mark.django_db
def test_loan_creation_decreases_book_quantity(
    book_for_loan_tests, patron_for_loan_tests
):
    book = book_for_loan_tests
    initial_quantity = book.quantity
    Loan.objects.create(
        book=book, patron=patron_for_loan_tests, due_date=timezone.now()
    )
    book.refresh_from_db()
    assert book.quantity == initial_quantity - 1


@pytest.mark.django_db
def test_loan_return_increases_book_quantity(
    book_for_loan_tests, patron_for_loan_tests
):
    loan = Loan.objects.create(
        book=book_for_loan_tests, patron=patron_for_loan_tests, due_date=timezone.now()
    )
    initial_quantity = book_for_loan_tests.quantity
    loan.is_returned = True
    loan.save()
    book_for_loan_tests.refresh_from_db()
    assert book_for_loan_tests.quantity == initial_quantity + 1


@pytest.mark.django_db
def test_unreturning_loan_decreases_book_quantity(
    book_for_loan_tests, patron_for_loan_tests
):
    loan = Loan.objects.create(
        book=book_for_loan_tests, patron=patron_for_loan_tests, due_date=timezone.now()
    )
    loan.is_returned = True
    loan.save()
    initial_quantity = book_for_loan_tests.quantity
    loan.is_returned = False
    loan.save()
    book_for_loan_tests.refresh_from_db()
    assert book_for_loan_tests.quantity == initial_quantity - 1


@pytest.mark.django_db
def test_cannot_loan_book_with_zero_quantity(
    patron_for_loan_tests, book_for_loan_tests
):
    book_for_loan_tests.quantity = 0
    book_for_loan_tests.save()
    with pytest.raises(
        ValueError, match="Não há exemplares deste livro disponíveis para empréstimo."
    ):
        Loan.objects.create(
            book=book_for_loan_tests,
            patron=patron_for_loan_tests,
            due_date=timezone.now(),
        )


@pytest.mark.django_db
def test_cannot_unreturn_loan_if_no_stock(book_for_loan_tests, patron_for_loan_tests):
    loan = Loan.objects.create(
        book=book_for_loan_tests, patron=patron_for_loan_tests, due_date=timezone.now()
    )
    loan.is_returned = True
    loan.save()
    book_for_loan_tests.quantity = 0
    book_for_loan_tests.save()
    loan.is_returned = False
    with pytest.raises(
        ValueError, match="Não é possível reverter a devolução, pois não há estoque."
    ):
        loan.save()


@pytest.mark.django_db
def test_loan_form_invalid_for_book_with_zero_quantity(
    book_for_loan_tests, patron_for_loan_tests
):
    book_for_loan_tests.quantity = 0
    book_for_loan_tests.save()
    form_data = {
        "book": book_for_loan_tests.pk,
        "patron": patron_for_loan_tests.pk,
        "due_date": timezone.now(),
    }
    form = LoanForm(data=form_data)
    assert not form.is_valid()
    assert (
        "Não há exemplares disponíveis para empréstimo deste livro."
        in form.errors["__all__"]
    )


@pytest.mark.django_db
def test_loan_list_view_and_search(
    authenticated_client_for_loans, book_for_loan_tests, patron_for_loan_tests
):
    Loan.objects.create(
        book=book_for_loan_tests, patron=patron_for_loan_tests, due_date=timezone.now()
    )
    url = reverse("loans:list")
    response = authenticated_client_for_loans.get(url)
    assert response.status_code == 200
    assert book_for_loan_tests.title in response.content.decode("utf-8")
    search_url = f"{url}?q={patron_for_loan_tests.name}"
    response_search = authenticated_client_for_loans.get(search_url)
    assert response_search.status_code == 200
    assert book_for_loan_tests.title in response_search.content.decode("utf-8")


@pytest.mark.django_db
def test_loan_create_view_post(
    authenticated_client_for_loans, book_for_loan_tests, patron_for_loan_tests
):
    url = reverse("loans:create")
    form_data = {
        "book": book_for_loan_tests.pk,
        "patron": patron_for_loan_tests.pk,
        "due_date": (timezone.now() + timedelta(days=15)).strftime("%Y-%m-%dT%H:%M"),
    }
    response = authenticated_client_for_loans.post(url, data=form_data)
    assert response.status_code == 302
    assert Loan.objects.count() == 1


@pytest.mark.django_db
def test_loan_detail_view(
    authenticated_client_for_loans, book_for_loan_tests, patron_for_loan_tests
):
    loan = Loan.objects.create(
        book=book_for_loan_tests, patron=patron_for_loan_tests, due_date=timezone.now()
    )
    url = reverse("loans:detail", kwargs={"pk": loan.pk})
    response = authenticated_client_for_loans.get(url)
    assert response.status_code == 200
    assert patron_for_loan_tests.name in response.content.decode("utf-8")


@pytest.mark.django_db
def test_loan_update_view_post(
    authenticated_client_for_loans, book_for_loan_tests, patron_for_loan_tests
):
    loan = Loan.objects.create(
        book=book_for_loan_tests, patron=patron_for_loan_tests, due_date=timezone.now()
    )
    url = reverse("loans:update", kwargs={"pk": loan.pk})
    new_notes = "Nota de teste atualizada"
    form_data = {
        "book": book_for_loan_tests.pk,
        "patron": patron_for_loan_tests.pk,
        "due_date": loan.due_date.strftime("%Y-%m-%dT%H:%M"),
        "notes": new_notes,
    }
    response = authenticated_client_for_loans.post(url, data=form_data)
    assert response.status_code == 302
    loan.refresh_from_db()
    assert loan.notes == new_notes


@pytest.mark.django_db
def test_loan_delete_view_post(
    authenticated_client_for_loans, book_for_loan_tests, patron_for_loan_tests
):
    loan = Loan.objects.create(
        book=book_for_loan_tests, patron=patron_for_loan_tests, due_date=timezone.now()
    )
    url = reverse("loans:delete", kwargs={"pk": loan.pk})
    response = authenticated_client_for_loans.post(url)
    assert response.status_code == 302
    assert not Loan.objects.filter(pk=loan.pk).exists()


@pytest.mark.django_db
def test_loan_return_view_post(
    authenticated_client_for_loans, book_for_loan_tests, patron_for_loan_tests
):
    loan = Loan.objects.create(
        book=book_for_loan_tests, patron=patron_for_loan_tests, due_date=timezone.now()
    )
    url = reverse("loans:return", kwargs={"pk": loan.pk})
    form_data = {"book": book_for_loan_tests.pk, "notes": loan.notes}
    response = authenticated_client_for_loans.post(url, data=form_data)
    assert response.status_code == 302
    loan.refresh_from_db()
    assert loan.is_returned


@pytest.mark.django_db
def test_returned_loan_list_view_and_search(
    authenticated_client_for_loans, book_for_loan_tests, patron_for_loan_tests
):
    loan = Loan.objects.create(
        book=book_for_loan_tests, patron=patron_for_loan_tests, due_date=timezone.now()
    )
    loan.is_returned = True
    loan.save()
    url = reverse("loans:returned-list")
    response = authenticated_client_for_loans.get(url)
    assert response.status_code == 200
    assert book_for_loan_tests.title in response.content.decode("utf-8")
    search_url = f"{url}?q={book_for_loan_tests.title}"
    response_search = authenticated_client_for_loans.get(search_url)
    assert response_search.status_code == 200
    assert book_for_loan_tests.title in response_search.content.decode("utf-8")


@pytest.mark.django_db
def test_returned_loan_detail_view(
    authenticated_client_for_loans, book_for_loan_tests, patron_for_loan_tests
):
    loan = Loan.objects.create(
        book=book_for_loan_tests, patron=patron_for_loan_tests, due_date=timezone.now()
    )
    loan.is_returned = True
    loan.save()
    url = reverse("loans:returned-detail", kwargs={"pk": loan.pk})
    response = authenticated_client_for_loans.get(url)
    assert response.status_code == 200
    assert patron_for_loan_tests.name in response.content.decode("utf-8")
