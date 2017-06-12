from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

def home(request):
    return render(request, 'fh17/home.html')
