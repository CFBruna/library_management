from django.urls import path

from . import views

app_name = "categories"

urlpatterns = [
    path(
        "list/",
        views.CategoryListView.as_view(),
        name="list",
    ),
    path(
        "<int:pk>/detail/",
        views.CategoryDetailView.as_view(),
        name="detail",
    ),
    path(
        "create/",
        views.CategoryCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update/",
        views.CategoryUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete/",
        views.CategoryDeleteView.as_view(),
        name="delete",
    ),
]
