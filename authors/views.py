from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
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


class AuthorCreateView(
    LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView
):
    model = models.Author
    template_name = "authors/author_create.html"
    form_class = forms.AuthorForm
    success_url = reverse_lazy("authors:list")
    permission_required = "authors.add_author"
    success_message = "Autor(a) cadastrado(a) com sucesso!"


class AuthorDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Author
    template_name = "authors/author_detail.html"
    permission_required = "authors.view_author"


class AuthorUpdateView(
    LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView
):
    model = models.Author
    template_name = "authors/author_update.html"
    form_class = forms.AuthorForm
    success_url = reverse_lazy("authors:list")
    permission_required = "authors.change_author"
    success_message = "Dados do(a) autor(a) atualizados com sucesso!"


class AuthorDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Author
    template_name = "authors/author_delete.html"
    success_url = reverse_lazy("authors:list")
    permission_required = "authors.delete_author"

    def form_valid(self, form):
        messages.success(
            self.request,
            f"O(A) autor(a) '{self.object.name}' foi deletado(a) com sucesso.",
        )
        return super().form_valid(form)
