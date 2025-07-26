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


class PatronListView(ListView):
    model = models.Patron
    template_name = "patrons/patron_list.html"
    context_object_name = "patrons"

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get("q")

        if search:
            queryset = queryset.filter(
                Q(name__icontains=search) | Q(cpf__icontains=search)
            )

        return queryset


class PatronDetailView(DetailView):
    model = models.Patron
    template_name = "patrons/patron_detail.html"


class PatronCreateView(CreateView):
    model = models.Patron
    template_name = "patrons/patron_create.html"
    form_class = forms.PatronForm
    success_url = reverse_lazy("patron-list")


class PatronUpdateView(UpdateView):
    model = models.Patron
    template_name = "patrons/patron_update.html"
    form_class = forms.PatronForm
    success_url = reverse_lazy("patron-list")


class PatronDeleteView(DeleteView):
    model = models.Patron
    template_name = "patrons/patron_delete.html"
    success_url = reverse_lazy("patron-list")
