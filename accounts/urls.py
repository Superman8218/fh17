from django.conf.urls import url

from views import LoginView, logout_view, register_view

urlpatterns = [
        url(r'^login/$', LoginView.as_view(), name='login'),
        url(r'^logout/$', logout_view, name='logout'),
        url(r'^register/$', register_view, name='register'),
]
