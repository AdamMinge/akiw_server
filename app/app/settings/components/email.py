from environ import Env

env = Env()
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_USE_TLS = env.bool("EMAIL_USE_TLS", default=False)
EMAIL_HOST = env.str("EMAIL_HOST")
EMAIL_PORT = env.int("EMAIL_PORT")
EMAIL_HOST_USER = env.str("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env.str("EMAIL_HOST_PASSWORD")
