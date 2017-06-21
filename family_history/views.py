# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse

from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from django.contrib.auth.mixins import LoginRequiredMixin

from forms import ProgressForm

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'family_history/dashboard.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DashboardView, self).get_context_data(*args, **kwargs)
        context['stats'] = self.request.user.profile.familyhistorystats
        return context


class ProgressFormView(LoginRequiredMixin, FormView):
    template_name = 'family_history/progress-form.html'
    form_class = ProgressForm

    def form_valid(self, form):
        user_stats = self.request.user.profile.familyhistorystats

        if form.cleaned_data['generations']:
            user_stats.generations = form.cleaned_data['generations']

        if form.cleaned_data['indexed']:
            user_stats.indexed += form.cleaned_data['indexed']

        if form.cleaned_data['memories']:
            user_stats.memories += form.cleaned_data['memories']

        if form.cleaned_data['names']:
            user_stats.names += form.cleaned_data['names']

        user_stats.save()

        # Redirects to the success_url
        return super(ProgressFormView, self).form_valid(form)

    def get_success_url(self):
        messages.add_message(self.request, messages.INFO, 'Thank you, your stats have been updated.')
        return reverse('fh:dashboard')

class ReportsView(TemplateView):
    template_name = 'family_history/reports.html'
