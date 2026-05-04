from core.settings.get_env import env

SECRET_KEY = env("SECRET_KEY")

if env("PYTHON_ENVIRONMENT") == "PRODUCTION":
    ALLOWED_HOSTS = ["localhost", "127.0.0.1", "[::1]"]

    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True

    CSRF_TRUSTED_ORIGINS = ["http://localhost:1337"]
