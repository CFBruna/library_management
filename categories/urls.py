from django.urls import path

from . import views

urlpatterns = [
    path(
        "categories/list/",
        views.CategoryListView.as_view(),
        name="category-list",
    ),
    path(
        "categories/<int:pk>/detail/",
        views.CategoryDetailView.as_view(),
        name="category-detail",
    ),
    path(
        "categories/create/",
        views.CategoryCreateView.as_view(),
        name="category-create",
    ),
    path(
        "categories/<int:pk>/update/",
        views.CategoryUpdateView.as_view(),
        name="category-update",
    ),
    path(
        "categories/<int:pk>/delete/",
        views.CategoryDeleteView.as_view(),
        name="category-delete",
    ),
]
