from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from accounts.forms import RegisterForm


class Login(LoginView):
    """Log a user into Cyberlab."""

    template_name = "accounts/auth/login.html"
    redirect_authenticated_user = True


def register(request: HttpRequest) -> HttpResponse:
    """Create a new Cyberlab user."""

    if request.user.is_authenticated:
        return redirect("profile")

    form = RegisterForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect("profile")

    return render(
        request,
        "accounts/auth/register.html",
        {"form": form},
    )


@login_required
def profile(request: HttpRequest) -> HttpResponse:
    """Show the currently logged-in user's profile."""

    return render(request, "accounts/profile.html")
