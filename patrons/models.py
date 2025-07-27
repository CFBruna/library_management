from django.core.validators import RegexValidator
from django.db import models

phone_validator = RegexValidator(
    regex=r"^(\+55)?\d{10,11}$",
    message="Número inválido. Formato esperado: +5511999998888 ou 11999999999.",
)

cpf_validator = RegexValidator(
    regex=r"^\d{11}$", message="CPF deve ter 11 dígitos numéricos."
)


class Patron(models.Model):
    name = models.CharField("Nome", max_length=250)
    phone_number = models.CharField(
        "Telefone", max_length=13, validators=[phone_validator]
    )
    email = models.EmailField("Email", unique=True)
    cpf = models.CharField(
        "CPF", max_length=11, unique=True, validators=[cpf_validator]
    )
    address = models.TextField("Endereço", blank=True)
    description = models.TextField("Descrição", blank=True)

    class Meta:
        verbose_name = "Leitor"
        verbose_name_plural = "Leitores"

    def __str__(self):
        return f"{self.name} (CPF: {self.cpf})"
