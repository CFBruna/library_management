from django import forms

from . import models


class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = [
            "title",
            "author",
            "category",
            "page_count",
            "isbn",
            "quantity",
        ]
        labels = {
            "title": "Título",
            "author": "Autor(es)",
            "category": "Categoria",
            "page_count": "Número de Páginas",
            "isbn": "ISBN",
            "quantity": "Quantidade",
        }
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.SelectMultiple(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "page_count": forms.NumberInput(attrs={"class": "form-control"}),
            "isbn": forms.TextInput(attrs={"class": "form-control"}),
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
        }
