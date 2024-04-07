"""
Django settings for a Hurricane-based project.

For the full list of settings and their config, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from django.utils.translation import pgettext_lazy as _

from decouple import config

from configuration.components import BASE_DIR


DEBUG = config("DJANGO_DEBUG", cast=bool, default=False)


ROOT_URLCONF = "configuration.urls"

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-us"

USE_I18N = True
USE_L10N = True

LANGUAGES = (("en", _("English")),)

LOCALE_PATHS = ("locale/",)

USE_TZ = True
TIME_ZONE = "UTC"


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Templates

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            # Contains plain text templates, like `robots.txt`:
            BASE_DIR / "templates",
        ],
        "OPTIONS": {
            "context_processors": [
                # Default template context processors:
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.request",
            ],
            "loaders":[(
                "django.template.loaders.cached.Loader", [
                    "django.template.loaders.filesystem.Loader",
                    "django.template.loaders.app_directories.Loader",
                    "django_components.template_loader.Loader",
                ]
            )],
            "builtins": [
                "django_components.templatetags.component_tags",
            ]
        },
    }
]


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Security
SECRET_KEY = config("DJANGO_SECRET_KEY")
ALLOWED_HOSTS = config("DJANGO_ALLOWED_HOSTS", cast=list, default=["*"])
SESSION_COOKIE_HTTPONLY = config("DJANGO_SESSION_COOKIE_HTTPONLY", cast=bool, default=True)
CSRF_COOKIE_HTTPONLY = config("DJANGO_CSRF_COOKIE_HTTPONLY", cast=bool, default=True)
SECURE_CONTENT_TYPE_NOSNIFF = config("DJANGO_SECURE_CONTENT_TYPE_NOSNIFF", cast=bool, default=True)
SECURE_BROWSER_XSS_FILTER = config("DJANGO_SECURE_BROWSER_XSS_FILTER", cast=bool, default=True)

X_FRAME_OPTIONS = config("DJANGO_X_FRAME_OPTIONS", default="DENY")

# https://github.com/DmytroLitvinov/django-http-referrer-policy
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy
REFERRER_POLICY = config("DJANGO_REFERRER_POLICY", default="same-origin")

EMAIL_TIMEOUT = 5

with open(os.path.join(BASE_DIR, "version.txt")) as v_file:
    VERSION = v_file.read()

HURRICANE_VERSION = VERSION

COMPRESS_ROOT = BASE_DIR / "static"
COMPRESS_ENABLED = True

COMPONENTS = {
    "RENDER_DEPENDENCIES": True
}
