from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from . import forms, models


class LoanListView(ListView):
    model = models.Loan
    template_name = "loans/loan_list.html"
    context_object_name = "loans"

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get("q")
        queryset = queryset.filter(is_returned=False)

        if search:
            queryset = queryset.filter(
                Q(book__title__icontains=search)
                | Q(patron__name__icontains=search)
                | Q(patron__cpf__icontains=search)
            )

        return queryset


class LoanDetailView(DetailView):
    model = models.Loan
    template_name = "loans/loan_detail.html"


class LoanCreateView(CreateView):
    model = models.Loan
    template_name = "loans/loan_create.html"
    form_class = forms.LoanForm
    success_url = reverse_lazy("loan-list")

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields.pop("is_returned")
        return form


class LoanUpdateView(UpdateView):
    model = models.Loan
    template_name = "loans/loan_update.html"
    form_class = forms.LoanForm
    success_url = reverse_lazy("loan-list")

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields.pop("is_returned")
        return form


class LoanDeleteView(DeleteView):
    model = models.Loan
    template_name = "loans/loan_delete.html"
    success_url = reverse_lazy("loan-list")


class LoanReturnView(UpdateView):
    model = models.Loan
    template_name = "loans/loan_return.html"
    form_class = forms.LoanForm
    success_url = reverse_lazy("loan-list")

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        for field in ["book", "patron", "due_date", "is_returned"]:
            form.fields.pop(field)
        return form

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.is_returned = True
        self.object.save()
        return super().form_valid(form)


class LoanReturnedListView(ListView):
    model = models.Loan
    template_name = "loans/loan_returned_list.html"
    context_object_name = "loans"

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get("q")
        queryset = queryset.filter(is_returned=True)

        if search:
            queryset = queryset.filter(
                Q(book__title__icontains=search)
                | Q(patron__name__icontains=search)
                | Q(patron__cpf__icontains=search)
            )

        return queryset


class LoanReturnedDetailView(DetailView):
    model = models.Loan
    template_name = "loans/loan_returned_detail.html"
