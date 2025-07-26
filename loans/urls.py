from django.urls import path

from . import views

urlpatterns = [
    path("loans/list/", views.LoanListView.as_view(), name="loan-list"),
    path(
        "loans/<int:pk>/detail/",
        views.LoanDetailView.as_view(),
        name="loan-detail",
    ),
    path("loans/create/", views.LoanCreateView.as_view(), name="loan-create"),
    path(
        "loans/<int:pk>/update/",
        views.LoanUpdateView.as_view(),
        name="loan-update",
    ),
    path(
        "loans/<int:pk>/delete/",
        views.LoanDeleteView.as_view(),
        name="loan-delete",
    ),
    path(
        "loans/<int:pk>/return/",
        views.LoanReturnView.as_view(),
        name="loan-return",
    ),
    path(
        "loans/returned/",
        views.LoanReturnedListView.as_view(),
        name="loan-returned-list",
    ),
    path(
        "loans/<int:pk>/returned/detail/",
        views.LoanReturnedDetailView.as_view(),
        name="loan-returned-detail",
    ),
]
