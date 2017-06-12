from django.conf.urls import url

from views import dashboard, base

urlpatterns = [
        url(r'^$', base, name='base'),
        url(r'^dashboard$', dashboard, name='dashboard'),
]
