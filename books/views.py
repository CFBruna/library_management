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


class BookListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Book
    template_name = "books/book_list.html"
    context_object_name = "books"
    permission_required = "books.view_book"

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get("q")

        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) | Q(isbn__icontains=search)
            )

        return queryset


class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Book
    template_name = "books/book_detail.html"
    permission_required = "books.view_book"


class BookCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Book
    template_name = "books/book_create.html"
    form_class = forms.BookForm
    success_url = reverse_lazy("books:list")
    permission_required = "books.add_book"


class BookUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Book
    template_name = "books/book_update.html"
    form_class = forms.BookForm
    success_url = reverse_lazy("books:list")
    permission_required = "books.change_book"


class BookDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Book
    template_name = "books/book_delete.html"
    success_url = reverse_lazy("books:list")
    permission_required = "books.delete_book"
