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


class BookListView(ListView):
    model = models.Book
    template_name = "books/book_list.html"
    context_object_name = "books"

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get("q")

        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) | Q(isbn__icontains=search)
            )

        return queryset


class BookDetailView(DetailView):
    model = models.Book
    template_name = "books/book_detail.html"


class BookCreateView(CreateView):
    model = models.Book
    template_name = "books/book_create.html"
    form_class = forms.BookForm
    success_url = reverse_lazy("book-list")


class BookUpdateView(UpdateView):
    model = models.Book
    template_name = "books/book_update.html"
    form_class = forms.BookForm
    success_url = reverse_lazy("book-list")


class BookDeleteView(DeleteView):
    model = models.Book
    template_name = "books/book_delete.html"
    success_url = reverse_lazy("book-list")
