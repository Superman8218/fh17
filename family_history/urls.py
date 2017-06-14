from django.conf.urls import url

from views import dashboard, base, ProgressFormView

urlpatterns = [
        url(r'^$', base, name='base'),
        url(r'^dashboard$', dashboard, name='dashboard'),
        url(r'^progress$', ProgressFormView.as_view(), name='progress'),
]
