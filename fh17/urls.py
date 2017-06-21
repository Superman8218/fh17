"""fh17 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include

from fh17.views import HomeView
from fh17.views import ContactView
from fh17.views import ReportsView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^contact$', ContactView.as_view(), name='contact'),
    url(r'^reports$', ReportsView.as_view(), name='reports'),
    url(r'^fh/', include('family_history.urls', namespace='fh')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^profiles/', include('profiles.urls', namespace='profiles')),
]
