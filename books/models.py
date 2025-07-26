from django.db import models

from authors.models import Author
from categories.models import Category


class Book(models.Model):
    title = models.CharField("Título", max_length=250)
    author = models.ManyToManyField(
        Author, related_name="books", verbose_name="Autor(es)"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="books",
        verbose_name="Categoria",
    )
    page_count = models.PositiveIntegerField("Número de Páginas")
    isbn = models.CharField("ISBN", max_length=17, unique=True)
    quantity = models.PositiveIntegerField("Quantidade", default=0)

    class Meta:
        verbose_name = "Livro"
        verbose_name_plural = "Livros"

    def __str__(self):
        return f"{self.title} (ISBN: {self.isbn})"
