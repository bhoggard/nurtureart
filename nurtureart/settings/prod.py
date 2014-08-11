from .base import *

DEBUG = False
TEMPLATE_DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = ['nurtureart.artcat.com']

PROJECT_DIR = Path(__file__).ancestor(4)
MEDIA_ROOT = PROJECT_DIR.child("media")
STATIC_ROOT = PROJECT_DIR.child("static")
