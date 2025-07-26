from django.db import models


class Author(models.Model):
    name = models.CharField("Nome", max_length=250)
    description = models.TextField("Descrição", blank=True, null=True)

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

    def __str__(self):
        return self.name
