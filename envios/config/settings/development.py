import os

from .base import *


DEBUG = True

SECRET_KEY = '6fin=)xzbvc*khuhh@^%6)zoasj&g4#i&-iaofu7d)06b!5qy2'

ALLOWED_HOSTS = ['*']

# Database

DATABASES_DEFAULT = 'sqlite:////%s' % BASE_DIR.child('db.sqlite3')

DATABASES = {
    'default': dj_database_url.config(default=DATABASES_DEFAULT)
}