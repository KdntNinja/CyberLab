from typing import cast

import pytest
from django.http import HttpResponseRedirect
from django.test import Client
from django.urls import reverse

from accounts.models import User

pytestmark = pytest.mark.django_db


def test_dashboard_requires_login() -> None:
    client = Client()

    response = client.get(reverse("dashboard"))

    assert response.status_code == 302

    redirect_response = cast(HttpResponseRedirect, response)

    assert redirect_response.url == f"{reverse('login')}?next=/dash/"


def test_dashboard_returns_success_when_logged_in() -> None:
    user = User.objects.create_user(
        username="testuser",
        password="testpassword123",
    )

    client = Client()
    client.force_login(user)

    response = client.get(reverse("dashboard"))

    assert response.status_code == 200


def test_dashboard_contains_project_name() -> None:
    user = User.objects.create_user(
        username="testuser",
        password="testpassword123",
    )

    client = Client()
    client.force_login(user)

    response = client.get(reverse("dashboard"))

    assert b"Cyberlab" in response.content
