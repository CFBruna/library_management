from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
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


class LoanListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Loan
    template_name = "loans/loan_list.html"
    context_object_name = "loans"
    permission_required = "loans.view_loan"

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


class LoanDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Loan
    template_name = "loans/loan_detail.html"
    permission_required = "loans.view_loan"


class LoanCreateView(
    LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView
):
    model = models.Loan
    template_name = "loans/loan_create.html"
    form_class = forms.LoanForm
    success_url = reverse_lazy("loans:list")
    permission_required = "loans.add_loan"
    success_message = "Empréstimo cadastrado com sucesso."

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields.pop("is_returned")
        return form


class LoanUpdateView(
    LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView
):
    model = models.Loan
    template_name = "loans/loan_update.html"
    form_class = forms.LoanForm
    success_url = reverse_lazy("loans:list")
    permission_required = "loans.change_loan"
    success_message = "Empréstimo atualizado com sucesso."

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields.pop("is_returned")
        return form


class LoanDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Loan
    template_name = "loans/loan_delete.html"
    success_url = reverse_lazy("loans:list")
    permission_required = "loans.delete_loan"

    def form_valid(self, form):
        messages.success(
            self.request,
            f"O empréstimo para '{self.object.patron.name}' foi deletado com sucesso.",
        )
        return super().form_valid(form)


class LoanReturnView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Loan
    template_name = "loans/loan_return.html"
    form_class = forms.LoanForm
    success_url = reverse_lazy("loans:list")
    permission_required = "loans.view_loan"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        for field in ["patron", "due_date", "is_returned"]:
            form.fields.pop(field)
        return form

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.is_returned = True
        self.object.save()
        messages.success(
            self.request,
            f"O livro '{self.object.book.title}' foi devolvido com sucesso.",
        )
        return super().form_valid(form)


class LoanReturnedListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Loan
    template_name = "loans/loan_returned_list.html"
    context_object_name = "loans"
    permission_required = "loans.view_loan"

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


class LoanReturnedDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Loan
    template_name = "loans/loan_returned_detail.html"
    permission_required = "loans.view_loan"
