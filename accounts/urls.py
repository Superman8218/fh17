from django.conf.urls import url

from views import LoginView, logout, register

urlpatterns = [
        url(r'^login/$', LoginView.as_view(), name='login'),
        url(r'^logout/$', logout, name='logout'),
        url(r'^register/$', register, name='register'),
]
