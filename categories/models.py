from django.db import models


class Category(models.Model):
    name = models.CharField("Nome", max_length=250)
    description = models.TextField("Descrição", blank=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.name
