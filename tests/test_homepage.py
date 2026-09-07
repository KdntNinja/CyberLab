from django.test import Client
from django.urls import reverse


def test_homepage_returns_success() -> None:
    client = Client()

    response = client.get(reverse("home"))

    assert response.status_code == 200


def test_homepage_contains_project_name() -> None:
    client = Client()

    response = client.get(reverse("home"))

    assert b"Cyberlab" in response.content
