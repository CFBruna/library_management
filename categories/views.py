from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from . import forms, models


class CategoryListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Category
    template_name = "categories/category_list.html"
    context_object_name = "categories"
    permission_required = "categories.view_category"

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get("name")

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


class CategoryDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Category
    template_name = "categories/category_detail.html"
    permission_required = "categories.view_category"


class CategoryCreateView(
    LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView
):
    model = models.Category
    template_name = "categories/category_create.html"
    form_class = forms.CategoryForm
    success_url = reverse_lazy("categories:list")
    permission_required = "categories.add_category"
    success_message = "Categoria cadastrada com sucesso."


class CategoryUpdateView(
    LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView
):
    model = models.Category
    template_name = "categories/category_update.html"
    form_class = forms.CategoryForm
    success_url = reverse_lazy("categories:list")
    permission_required = "categories.change_category"
    success_message = "Categoria atualizada com sucesso."


class CategoryDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Category
    template_name = "categories/category_delete.html"
    success_url = reverse_lazy("categories:list")
    permission_required = "categories.delete_category"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        try:
            self.object.delete()
            messages.success(
                self.request,
                f"A categoria '{self.object.name}' foi deletada com sucesso.",
            )
            return redirect(self.success_url)
        except ProtectedError:
            messages.error(
                self.request,
                f"A categoria '{self.object.name}' não pode ser deletada, pois está sendo referenciada por um ou mais livros.",
            )
            return redirect(self.success_url)
