from django.contrib.auth.models import AbstractUser

from accounts.models import User


def test_custom_user_extends_abstract_user() -> None:
    assert issubclass(User, AbstractUser)
