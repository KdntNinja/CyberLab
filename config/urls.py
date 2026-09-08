from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("dash/", views.dashboard, name="dashboard"),
    path("users/", include("accounts.urls")),
    path("rooms/", include("rooms.urls")),
    path("admin/", admin.site.urls),
]
