from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

#############################################################################
# EMAIL configuration
#############################################################################

# For DEVELOPMENT use ONLY ONE of this
#
# The file backend writes emails to a file. A new file is
# created for each new session that is opened on this backend.
# ------------------------------------------------------------
#
# EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
# EMAIL_FILE_PATH = '/tmp/app-messages' # change this to a proper location

# The console backend just writes the emails that
# would be sent to the standard output.
# ------------------------------------------------------------
#
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
