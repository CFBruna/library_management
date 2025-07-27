from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("authors/", include("authors.urls")),
    path("books/", include("books.urls")),
    path("categories/", include("categories.urls")),
    path("loans/", include("loans.urls")),
    path("patrons/", include("patrons.urls")),
]
