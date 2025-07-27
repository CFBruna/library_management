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


class CategoryCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Category
    template_name = "categories/category_create.html"
    form_class = forms.CategoryForm
    success_url = reverse_lazy("category-list")
    permission_required = "categories.add_category"


class CategoryUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Category
    template_name = "categories/category_update.html"
    form_class = forms.CategoryForm
    success_url = reverse_lazy("category-list")
    permission_required = "categories.change_category"


class CategoryDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Category
    template_name = "categories/category_delete.html"
    success_url = reverse_lazy("category-list")
    permission_required = "categories.delete_category"
