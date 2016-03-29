import os


DEBUG = True

SECRET_KEY = 'secret key'

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')

CSRF_ENABLED = True

CSRF_SESSION_KEY = "secret"
