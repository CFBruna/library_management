from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from . import forms, models


class AuthorListView(ListView):
    model = models.Author
    template_name = "authors/author_list.html"
    context_object_name = "authors"

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get("name")

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


class AuthorCreateView(CreateView):
    model = models.Author
    template_name = "authors/author_create.html"
    form_class = forms.AuthorForm
    success_url = reverse_lazy("author-list")


class AuthorDetailView(DetailView):
    model = models.Author
    template_name = "authors/author_detail.html"


class AuthorUpdateView(UpdateView):
    model = models.Author
    template_name = "authors/author_update.html"
    form_class = forms.AuthorForm
    success_url = reverse_lazy("author-list")


class AuthorDeleteView(DeleteView):
    model = models.Author
    template_name = "authors/author_delete.html"
    success_url = reverse_lazy("author-list")
