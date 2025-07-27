from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
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


class PatronListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Patron
    template_name = "patrons/patron_list.html"
    context_object_name = "patrons"
    permission_required = "patrons.view_patron"

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get("q")

        if search:
            queryset = queryset.filter(
                Q(name__icontains=search) | Q(cpf__icontains=search)
            )

        return queryset


class PatronDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Patron
    template_name = "patrons/patron_detail.html"
    permission_required = "patrons.view_patron"


class PatronCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Patron
    template_name = "patrons/patron_create.html"
    form_class = forms.PatronForm
    success_url = reverse_lazy("patron-list")
    permission_required = "patrons.add_patron"


class PatronUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Patron
    template_name = "patrons/patron_update.html"
    form_class = forms.PatronForm
    success_url = reverse_lazy("patron-list")
    permission_required = "patrons.change_patron"


class PatronDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Patron
    template_name = "patrons/patron_delete.html"
    success_url = reverse_lazy("patron-list")
    permission_required = "patrons.delete_patron"
