from django.conf import settings

BASE_TEMPLATE = getattr(settings, 'BASE_TEMPLATE', 'base.html')
