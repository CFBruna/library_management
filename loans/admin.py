from django.contrib import admin

from . import models


class LoanAdmin(admin.ModelAdmin):
    list_display = (
        "book",
        "patron",
        "loan_date",
        "due_date",
        "is_returned",
    )
    search_fields = (
        "book__title",
        "patron__name",
    )
    list_filter = (
        "is_returned",
        "loan_date",
        "due_date",
        "book",
        "patron",
    )


admin.site.register(models.Loan, LoanAdmin)
