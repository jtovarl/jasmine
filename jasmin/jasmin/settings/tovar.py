from .base import *

STATIC_ROOT = '/webapps/jasmine/static/'

MEDIA_ROOT = '/webapps/jasmine/media/'

DEBUG = False

ALLOWED_HOSTS = ['*']

DOMAIN = "http://127.0.0.1:8000"

BASE_URL = 'http://149.56.192.136'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DATABASE_NAME', 'jasmin'),
        'USER': os.getenv('DATABASE_USER', 'root'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD', 'vicecity'),
        'HOST': os.getenv('DATABASE_HOST', '127.0.0.1'),
        # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',  # Set to empty string for default.
    },
}

#Jasmin telnet defaults, override in local_settings.py
TELNET_HOST = '127.0.0.1'
TELNET_PORT = 8990
TELNET_USERNAME = 'jcliadmin'
TELNET_PW = 'jclipwd'  # no alternative storing as plain text
TELNET_TIMEOUT = 10  # reasonable value for intranet.


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.CoreJSONRenderer',
        'rest_framework_swagger.renderers.SwaggerUIRenderer',
        'rest_framework_swagger.renderers.OpenAPIRenderer',
    ),
}

################################################################################
#                            Other settings                                    #
################################################################################


STANDARD_PROMPT = 'jcli : '  # There should be no need to change this
INTERACTIVE_PROMPT ='> '  # Prompt for interactive commands

#This should be OK for REST API - we are not generating URLs
#see https://www.djangoproject.com/weblog/2013/feb/19/security/#s-issue-host-header-poisoning

SWAGGER_SETTINGS = {
    'LOGIN_URL': 'rest_framework:login',
    'LOGOUT_URL': 'rest_framework:logout',
    'USE_SESSION_AUTH': True,
    'DOC_EXPANSION': 'list',
    'APIS_SORTER': 'alpha'
}