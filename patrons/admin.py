from django.contrib import admin

from . import models


class PatronAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "phone_number",
        "email",
        "cpf",
    )
    search_fields = (
        "name",
        "cpf",
        "email",
    )
    list_filter = ("name",)


admin.site.register(models.Patron, PatronAdmin)
