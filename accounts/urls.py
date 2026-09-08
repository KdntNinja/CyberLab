from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views
from .views import Login

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", Login.as_view(), name="login"),
    path(
        "logout/",
        LogoutView.as_view(next_page="/"),
        name="logout",
    ),
    path("profile/", views.profile, name="profile"),
]
