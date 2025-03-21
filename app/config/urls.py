from django.contrib import admin
from django.urls import include, path

from .views import HomeView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls"), name="accounts"),
]
