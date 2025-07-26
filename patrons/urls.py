from django.urls import path

from . import views

urlpatterns = [
    path("patrons/list/", views.PatronListView.as_view(), name="patron-list"),
    path(
        "patrons/<int:pk>/detail/",
        views.PatronDetailView.as_view(),
        name="patron-detail",
    ),
    path(
        "patrons/create/",
        views.PatronCreateView.as_view(),
        name="patron-create",
    ),
    path(
        "patrons/<int:pk>/update/",
        views.PatronUpdateView.as_view(),
        name="patron-update",
    ),
    path(
        "patrons/<int:pk>/delete/",
        views.PatronDeleteView.as_view(),
        name="patron-delete",
    ),
]
