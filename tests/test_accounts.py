import pytest
from django.test import Client
from django.urls import reverse

from accounts.models import User

pytestmark = pytest.mark.django_db


def test_registration_page_loads() -> None:
    client = Client()

    response = client.get(reverse("register"))

    assert response.status_code == 200


def test_valid_registration_creates_user() -> None:
    client = Client()

    response = client.post(
        reverse("register"),
        {
            "username": "testuser",
            "email": "test@example.com",
            "password1": "Strong-Test-Password-123!",
            "password2": "Strong-Test-Password-123!",
        },
    )

    assert response.status_code == 302
    assert User.objects.filter(username="testuser").exists()


def test_registration_logs_user_in() -> None:
    client = Client()

    client.post(
        reverse("register"),
        {
            "username": "testuser",
            "email": "test@example.com",
            "password1": "Strong-Test-Password-123!",
            "password2": "Strong-Test-Password-123!",
        },
    )

    response = client.get(reverse("profile"))

    assert response.status_code == 200


def test_registration_rejects_mismatched_passwords() -> None:
    client = Client()

    response = client.post(
        reverse("register"),
        {
            "username": "testuser",
            "email": "test@example.com",
            "password1": "Strong-Test-Password-123!",
            "password2": "Different-Test-Password-456!",
        },
    )

    assert response.status_code == 200
    assert not User.objects.filter(username="testuser").exists()


def test_registration_rejects_duplicate_username() -> None:
    User.objects.create_user(
        username="testuser",
        password="Strong-Test-Password-123!",
    )

    client = Client()

    response = client.post(
        reverse("register"),
        {
            "username": "testuser",
            "email": "another@example.com",
            "password1": "Another-Strong-Password-123!",
            "password2": "Another-Strong-Password-123!",
        },
    )

    assert response.status_code == 200
    assert User.objects.filter(username="testuser").count() == 1


def test_login_page_loads() -> None:
    client = Client()

    response = client.get(reverse("login"))

    assert response.status_code == 200


def test_valid_login_authenticates_user() -> None:
    User.objects.create_user(
        username="testuser",
        password="correct-password",
    )

    client = Client()

    response = client.post(
        reverse("login"),
        {
            "username": "testuser",
            "password": "correct-password",
        },
    )

    assert response.status_code == 302

    profile_response = client.get(reverse("profile"))

    assert profile_response.status_code == 200


def test_invalid_login_does_not_authenticate_user() -> None:
    User.objects.create_user(
        username="testuser",
        password="correct-password",
    )

    client = Client()

    response = client.post(
        reverse("login"),
        {
            "username": "testuser",
            "password": "wrong-password",
        },
    )

    assert response.status_code == 200

    profile_response = client.get(reverse("profile"))

    assert profile_response.status_code == 302


def test_profile_requires_login() -> None:
    client = Client()

    response = client.get(reverse("profile"))

    assert response.status_code == 302


def test_logged_in_user_can_view_profile() -> None:
    user = User.objects.create_user(
        username="testuser",
        password="test-password",
    )

    client = Client()
    client.force_login(user)

    response = client.get(reverse("profile"))

    assert response.status_code == 200


def test_profile_displays_username() -> None:
    user = User.objects.create_user(
        username="testuser",
        password="test-password",
    )

    client = Client()
    client.force_login(user)

    response = client.get(reverse("profile"))

    assert response.status_code == 200
    assert b"testuser" in response.content


def test_logout_logs_user_out() -> None:
    user = User.objects.create_user(
        username="testuser",
        password="test-password",
    )

    client = Client()
    client.force_login(user)

    response = client.post(reverse("logout"))

    assert response.status_code == 302

    profile_response = client.get(reverse("profile"))

    assert profile_response.status_code == 302


def test_logout_rejects_get_request() -> None:
    user = User.objects.create_user(
        username="testuser",
        password="test-password",
    )

    client = Client()
    client.force_login(user)

    response = client.get(reverse("logout"))

    assert response.status_code == 405
