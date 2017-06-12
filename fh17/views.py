from __future__ import unicode_literals

from django.shortcuts import render

def home(request):
    return render(request, 'fh17/home.html')

def contact(request):
    return render(request, 'fh17/contact.html')
