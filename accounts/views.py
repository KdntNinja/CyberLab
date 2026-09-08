from django.contrib.auth.views import LoginView


class Login(LoginView):
    template_name = "users/accounts/login.html"
