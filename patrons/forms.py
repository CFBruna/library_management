from django import forms

from . import models


class PatronForm(forms.ModelForm):
    class Meta:
        model = models.Patron
        fields = [
            "name",
            "phone_number",
            "email",
            "cpf",
            "address",
            "description",
        ]
        labels = {
            "name": "Nome",
            "phone_number": "Celular",
            "email": "Email",
            "cpf": "CPF",
            "address": "Endereço",
            "description": "Descrição",
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "phone_number": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "cpf": forms.TextInput(attrs={"class": "form-control"}),
            "address": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }
