# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse

from django.views.generic.edit import FormView

from forms import ProgressForm

def base(request):
    return render(request, 'family_history/fh.html')

def dashboard(request):
    return render(request, 'family_history/dashboard.html')

class ProgressFormView(FormView):
    template_name = 'family_history/progress-form.html'
    form_class = ProgressForm

    def get_success_url(self):
        messages.add_message(request, messages.INFO, 'form submission success')
        return reverse('family_history/dashboard.html')
