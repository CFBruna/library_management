from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("", include("authors.urls")),
    path("", include("books.urls")),
    path("", include("categories.urls")),
    path("", include("loans.urls")),
    path("", include("patrons.urls")),
]
