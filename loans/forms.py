from django import forms
from django.core.exceptions import ValidationError

from . import models


class LoanForm(forms.ModelForm):
    class Meta:
        model = models.Loan
        fields = [
            "book",
            "patron",
            "due_date",
            "is_returned",
            "notes",
        ]
        labels = {
            "book": "Livro",
            "patron": "Leitor",
            "due_date": "Previsão de Devolução",
            "is_returned": "Devolvido?",
            "notes": "Observações",
        }
        widgets = {
            "book": forms.Select(attrs={"class": "form-select"}),
            "patron": forms.Select(attrs={"class": "form-select"}),
            "due_date": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "datetime-local"}
            ),
            "is_returned": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "notes": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                }
            ),
        }

    def clean(self):
        cleaned_data = super().clean()
        book = cleaned_data.get("book")

        if book and not self.instance.pk:
            if book.quantity < 1:
                raise ValidationError(
                    "Não há exemplares disponíveis para empréstimo deste livro."
                )

        return cleaned_data
