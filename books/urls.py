from django.urls import path

from . import views

urlpatterns = [
    path("books/list/", views.BookListView.as_view(), name="book-list"),
    path(
        "books/<int:pk>/detail/",
        views.BookDetailView.as_view(),
        name="book-detail",
    ),
    path("books/create/", views.BookCreateView.as_view(), name="book-create"),
    path(
        "books/<int:pk>/update",
        views.BookUpdateView.as_view(),
        name="book-update",
    ),
    path(
        "books/<int:pk>/delete/",
        views.BookDeleteView.as_view(),
        name="book-delete",
    ),
]
