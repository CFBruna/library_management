from django.urls import path

from . import views

app_name = "loans"

urlpatterns = [
    path("list/", views.LoanListView.as_view(), name="list"),
    path(
        "<int:pk>/detail/",
        views.LoanDetailView.as_view(),
        name="detail",
    ),
    path("create/", views.LoanCreateView.as_view(), name="create"),
    path(
        "<int:pk>/update/",
        views.LoanUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete/",
        views.LoanDeleteView.as_view(),
        name="delete",
    ),
    path(
        "<int:pk>/return/",
        views.LoanReturnView.as_view(),
        name="return",
    ),
    path(
        "returned/",
        views.LoanReturnedListView.as_view(),
        name="returned-list",
    ),
    path(
        "<int:pk>/returned/detail/",
        views.LoanReturnedDetailView.as_view(),
        name="returned-detail",
    ),
]
