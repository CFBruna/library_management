from django.urls import path

from . import views

app_name = "patrons"

urlpatterns = [
    path("list/", views.PatronListView.as_view(), name="list"),
    path(
        "<int:pk>/detail/",
        views.PatronDetailView.as_view(),
        name="detail",
    ),
    path(
        "create/",
        views.PatronCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update/",
        views.PatronUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete/",
        views.PatronDeleteView.as_view(),
        name="delete",
    ),
]
