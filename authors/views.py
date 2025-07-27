from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from . import forms, models


class AuthorListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Author
    template_name = "authors/author_list.html"
    context_object_name = "authors"
    permission_required = "authors.view_author"

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get("name")

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


class AuthorCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Author
    template_name = "authors/author_create.html"
    form_class = forms.AuthorForm
    success_url = reverse_lazy("authors:list")
    permission_required = "authors.add_author"


class AuthorDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Author
    template_name = "authors/author_detail.html"
    permission_required = "authors.view_author"


class AuthorUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Author
    template_name = "authors/author_update.html"
    form_class = forms.AuthorForm
    success_url = reverse_lazy("authors:list")
    permission_required = "authors.change_author"


class AuthorDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Author
    template_name = "authors/author_delete.html"
    success_url = reverse_lazy("authors:list")
    permission_required = "authors.delete_author"
