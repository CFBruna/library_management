from django.contrib import admin

from . import models


class BookAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "isbn",
        "quantity",
        "category",
    )
    search_fields = (
        "title",
        "isbn",
        "author__name",
    )
    list_filter = (
        "title",
        "category__name",
    )


admin.site.register(models.Book, BookAdmin)
