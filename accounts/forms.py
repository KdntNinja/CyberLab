from django.contrib.auth.forms import UserCreationForm

from accounts.models import User


class RegisterForm(UserCreationForm[User]):
    """Form used to create a Cyberlab account."""

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")
