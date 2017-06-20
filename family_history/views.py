# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse

from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from django.contrib.auth.decorators import login_required

from forms import ProgressForm

@login_required
class DashboardView(TemplateView):
    template_name = 'family_history/dashboard.html'

@login_required
class ProgressFormView(FormView):
    template_name = 'family_history/progress-form.html'
    form_class = ProgressForm

    def get_success_url(self):
        messages.add_message(request, messages.INFO, 'form submission success')
        return reverse('fh:dashboard')

class ReportsView(TemplateView):
    template_name = 'family_history/reports.html'
