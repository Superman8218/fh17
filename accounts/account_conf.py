from django.conf import settings

BASE_TEMPLATE = getattr(settings, 'BASE_TEMPLATE', 'base.html')
UPDATE_PROFILE_URL = getattr(settings, 'UPDATE_PROFILE_URL', '')
LOGIN_TEMPLATE = getattr(settings, 'LOGIN_TEMPLATE', '')
REGISTRATION_TEMPLATE = getattr(settings, 'REGISTRATION_TEMPLATE', '')
