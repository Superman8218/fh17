from django.conf.urls import url

from views import ProfileUpdateView

urlpatterns = [
    url(r'^update/(?P<pk>[0-9]+)/$', ProfileUpdateView.as_view(), name='update'),
]
