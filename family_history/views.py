# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def base(request):
    return render(request, 'family_history/fh.html')

def dashboard(request):
    return render(request, 'family_history/dashboard.html')
