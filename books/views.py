from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError, Q
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


class BookCreateView(
    LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView
):
    model = models.Book
    template_name = "books/book_create.html"
    form_class = forms.BookForm
    success_url = reverse_lazy("books:list")
    permission_required = "books.add_book"
    success_message = "Livro cadastrado com sucesso."


class BookUpdateView(
    LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView
):
    model = models.Book
    template_name = "books/book_update.html"
    form_class = forms.BookForm
    success_url = reverse_lazy("books:list")
    permission_required = "books.change_book"
    success_message = "Livro atualizado com sucesso."


class BookDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Book
    template_name = "books/book_delete.html"
    success_url = reverse_lazy("books:list")
    permission_required = "books.delete_book"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        try:
            response = super().delete(request, *args, **kwargs)
            messages.success(
                self.request, f'O livro "{self.object.title}" foi removido com sucesso.'
            )
            return response
        except ProtectedError:
            messages.error(
                self.request,
                f'O livro "{self.object.title}" não pode ser removido, pois possui empréstimos ativos.',
            )
            return redirect("books:list")
