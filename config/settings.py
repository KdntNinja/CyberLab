import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")


def required_env(name: str) -> str:
    value = os.getenv(name)

    if value is None or not value.strip():
        raise RuntimeError(f"Required environment variable {name!r} is not set")

    return value.strip()


def env_bool(name: str, default: bool = False) -> bool:
    value = os.getenv(name)

    if value is None:
        return default

    normalized = value.strip().lower()

    if normalized in {"1", "true", "yes", "on"}:
        return True

    if normalized in {"0", "false", "no", "off"}:
        return False

    raise RuntimeError(f"Environment variable {name!r} must be a boolean value")


def env_int(name: str, default: int) -> int:
    value = os.getenv(name)

    if value is None:
        return default

    try:
        return int(value)
    except ValueError as exc:
        raise RuntimeError(f"Environment variable {name!r} must be an integer") from exc


def env_list(
    name: str,
    default: tuple[str, ...] = (),
) -> list[str]:
    value = os.getenv(name)

    if value is None or not value.strip():
        return list(default)

    return [item.strip() for item in value.split(",") if item.strip()]


ENVIRONMENT = os.getenv("DJANGO_ENV", "development").strip().lower()

if ENVIRONMENT not in {"development", "production"}:
    raise RuntimeError("DJANGO_ENV must be either 'development' or 'production'")

IS_PRODUCTION = ENVIRONMENT == "production"


# ---------------------------------------------------------------------------
# Core security
# ---------------------------------------------------------------------------

SECRET_KEY = required_env("DJANGO_SECRET_KEY")

if IS_PRODUCTION:
    if len(SECRET_KEY) < 50:
        raise RuntimeError("Production DJANGO_SECRET_KEY must be at least 50 characters long")

    if SECRET_KEY.startswith("django-insecure-"):
        raise RuntimeError("Do not use Django's generated insecure development key in production")

SECRET_KEY_FALLBACKS: list[str] = env_list("DJANGO_SECRET_KEY_FALLBACKS")

DEBUG = False if IS_PRODUCTION else env_bool("DJANGO_DEBUG", True)


def build_allowed_hosts() -> list[str]:
    if IS_PRODUCTION:
        allowed_hosts = env_list("DJANGO_ALLOWED_HOSTS")

        if not allowed_hosts:
            raise RuntimeError("DJANGO_ALLOWED_HOSTS must be configured in production")

        if "*" in allowed_hosts:
            raise RuntimeError("Wildcard ALLOWED_HOSTS is not permitted in production")

        return allowed_hosts

    return env_list(
        "DJANGO_ALLOWED_HOSTS",
        ("localhost", "127.0.0.1", "[::1]"),
    )


ALLOWED_HOSTS = build_allowed_hosts()


CSRF_TRUSTED_ORIGINS: list[str] = env_list("DJANGO_CSRF_TRUSTED_ORIGINS")


# ---------------------------------------------------------------------------
# Applications
# ---------------------------------------------------------------------------

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # CyberLab Apps
    "accounts.apps.AccountsConfig",
    "rooms.apps.RoomsConfig",
    "progress.apps.ProgressConfig",
    "challenges.apps.ChallengesConfig",
    "leaderboard.apps.LeaderboardConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    *(["whitenoise.middleware.WhiteNoiseMiddleware"] if IS_PRODUCTION else []),
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"
ASGI_APPLICATION = "config.asgi.application"


# ---------------------------------------------------------------------------
# Database
# ---------------------------------------------------------------------------
# Database
# ---------------------------------------------------------------------------


def build_databases() -> dict[str, dict[str, object]]:
    if IS_PRODUCTION:
        return {
            "default": {
                "ENGINE": "django.db.backends.postgresql",
                "NAME": required_env("DJANGO_DB_NAME"),
                "USER": required_env("DJANGO_DB_USER"),
                "PASSWORD": required_env("DJANGO_DB_PASSWORD"),
                "HOST": required_env("DJANGO_DB_HOST"),
                "PORT": required_env("DJANGO_DB_PORT"),
                "CONN_MAX_AGE": 60,
            }
        }

    return {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }


DATABASES = build_databases()


# ---------------------------------------------------------------------------
# Passwords
# ---------------------------------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.ScryptPasswordHasher",
]


# ---------------------------------------------------------------------------
# Internationalisation
# ---------------------------------------------------------------------------

LANGUAGE_CODE = "en-gb"

TIME_ZONE = "Europe/London"

USE_I18N = True
USE_TZ = True


# ---------------------------------------------------------------------------
# Static and media files
# ---------------------------------------------------------------------------

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"


def build_storages() -> dict[str, dict[str, str]]:
    static_backend = (
        "whitenoise.storage.CompressedManifestStaticFilesStorage"
        if IS_PRODUCTION
        else "django.contrib.staticfiles.storage.StaticFilesStorage"
    )

    return {
        "default": {
            "BACKEND": "django.core.files.storage.FileSystemStorage",
        },
        "staticfiles": {
            "BACKEND": static_backend,
        },
    }


STORAGES = build_storages()


# ---------------------------------------------------------------------------
# Browser / transport security
# ---------------------------------------------------------------------------

X_FRAME_OPTIONS = "DENY"

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_REFERRER_POLICY = "same-origin"
SECURE_CROSS_ORIGIN_OPENER_POLICY = "same-origin"

SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = "Lax"
CSRF_COOKIE_SAMESITE = "Lax"

SECURE_SSL_REDIRECT = IS_PRODUCTION
SESSION_COOKIE_SECURE = IS_PRODUCTION
CSRF_COOKIE_SECURE = IS_PRODUCTION

SECURE_HSTS_SECONDS = env_int("DJANGO_HSTS_SECONDS", 3600) if IS_PRODUCTION else 0

SECURE_HSTS_INCLUDE_SUBDOMAINS = (
    env_bool("DJANGO_HSTS_INCLUDE_SUBDOMAINS") if IS_PRODUCTION else False
)

SECURE_HSTS_PRELOAD = env_bool("DJANGO_HSTS_PRELOAD") if IS_PRODUCTION else False

TRUST_PROXY_HEADERS = IS_PRODUCTION and env_bool("DJANGO_TRUST_PROXY_HEADERS")

SECURE_PROXY_SSL_HEADER: tuple[str, str] | None = (
    ("HTTP_X_FORWARDED_PROTO", "https") if TRUST_PROXY_HEADERS else None
)


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Custom user model
AUTH_USER_MODEL = "accounts.User"

LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "home"
