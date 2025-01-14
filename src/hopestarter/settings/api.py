from .base import *
from .space import *
from .log import *
from .aws import *

try:
    from .drf import *
except ImportError:
    pass

ROOT_URLCONF = 'hopestarter.urls.api'

INSTALLED_APPS += (
    'oauth2_provider',
    'rest_framework',
    'rest_framework_gis',
    'social.apps.django_app.default',
    'rest_framework_social_oauth2',
    'django_filters',
    'hopecollector',
)

OAUTH2_PROVIDER = {
    'SCOPES': {
        'read': 'Read scope',
        'write': 'Write scope',
        'set-location': 'Set location',
        'update-profile': 'Update Profile'
    }
}

TEMPLATES[0]['OPTIONS']['context_processors'] += (
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
)

AUTHENTICATION_BACKENDS = (
    'rest_framework_social_oauth2.backends.DjangoOAuth2',
    'social.backends.twitter.TwitterOAuth',
    'django.contrib.auth.backends.ModelBackend',
)

SITE_ID = 2

GRAPPELLI_INDEX_DASHBOARD = 'hopecollector.dashboard.CustomIndexDashboard'

LOCATION_PERMS = ['IsAuthenticated', 'WeakTokenHasScope']
PROFILE_PERMS = ['IsAuthenticated', 'WeakTokenHasScope']
ETHNICITY_PERMS = ['IsAuthenticated', 'WeakTokenHasScope']

from .api_secret import *
