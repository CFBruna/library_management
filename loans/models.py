from django.db import models, transaction
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
        return f'Empréstimo de "{self.book}" para {self.patron.name} em {self.loan_date.strftime("%d/%m/%Y")}'

    def save(self, *args, **kwargs):

        if not self.pk:

            with transaction.atomic():
                if self.book.quantity > 0:
                    self.book.quantity -= 1
                    self.book.save()

                    super().save(*args, **kwargs)
                else:

                    raise ValueError("Não há exemplares deste livro disponíveis para empréstimo.")
            return


        else:

            if self.is_returned and not self.return_date:
                self.return_date = timezone.now()
            elif not self.is_returned and self.return_date:
                self.return_date = None 

            old_loan = Loan.objects.get(pk=self.pk)


            if self.is_returned and not old_loan.is_returned:
                with transaction.atomic():
                    self.book.quantity += 1
                    self.book.save()
                    super().save(*args, **kwargs)


            elif not self.is_returned and old_loan.is_returned:
                with transaction.atomic():
                    if self.book.quantity > 0:
                        self.book.quantity -= 1
                        self.book.save()
                        super().save(*args, **kwargs)
                    else:
                        raise ValueError("Não é possível reverter a devolução, pois não há estoque.")
            

            else:
                super().save(*args, **kwargs)
