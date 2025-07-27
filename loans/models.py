from django.db import models
from django.utils import timezone

from books.models import Book
from patrons.models import Patron


class Loan(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.PROTECT,
        related_name="loans",
        verbose_name="Livro",
    )
    patron = models.ForeignKey(
        Patron,
        on_delete=models.PROTECT,
        related_name="loans",
        verbose_name="Emprestado para",
    )
    loan_date = models.DateTimeField("Data do Empréstimo", auto_now_add=True)
    due_date = models.DateTimeField("Data prevista para devolução")
    is_returned = models.BooleanField("Devolvido?", default=False)
    return_date = models.DateTimeField("Data da devolução", blank=True, null=True)
    notes = models.TextField("Observações", blank=True)

    class Meta:
        verbose_name = "Empréstimo"
        verbose_name_plural = "Empréstimos"

    def __str__(self):
        return f'Empréstimo de "{self.book}" para {self.patron.name} em {
            self.loan_date.strftime("%d/%m/%Y")
        }'

    def save(self, *args, **kwargs):
        if self.pk:
            old = Loan.objects.get(pk=self.pk)
            was_returned = old.is_returned
        else:
            was_returned = False

        if self.is_returned and not self.return_date:
            self.return_date = timezone.now()

        is_new = not self.pk
        super().save(*args, **kwargs)

        if is_new and not self.is_returned:
            if self.book.quantity > 0:
                self.book.quantity -= 1
                self.book.save()

        elif self.is_returned and not was_returned:
            self.book.quantity += 1
            self.book.save()

        elif not self.is_returned and was_returned:
            if self.book.quantity > 0:
                self.book.quantity -= 1
                self.book.save()
