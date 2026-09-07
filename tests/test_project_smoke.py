import django

from config import settings


def test_django_project_loads() -> None:
    assert django.get_version()
    assert settings.ROOT_URLCONF == "config.urls"
