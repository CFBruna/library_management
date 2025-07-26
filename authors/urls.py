from django.urls import path

from . import views

urlpatterns = [
    path("authors/list/", views.AuthorListView.as_view(), name="author-list"),
    path(
        "authors/<int:pk>/detail/",
        views.AuthorDetailView.as_view(),
        name="author-detail",
    ),
    path(
        "authors/create/",
        views.AuthorCreateView.as_view(),
        name="author-create",
    ),
    path(
        "authors/<int:pk>/update/",
        views.AuthorUpdateView.as_view(),
        name="author-update",
    ),
    path(
        "authors/<int:pk>/delete/",
        views.AuthorDeleteView.as_view(),
        name="author-delete",
    ),
]
