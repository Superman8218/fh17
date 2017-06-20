from __future__ import unicode_literals

from django.views.generic.base import TemplateView

class HomeView(TemplateView):
    template_name = 'fh17/home.html'

class ContactView(TemplateView):
    template_name = 'fh17/contact.html'
