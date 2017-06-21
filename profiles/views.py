# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic.edit import UpdateView

from models import Profile

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'profiles/update.html'

    model = Profile
    fields = ('first_name', 'last_name', 'group')

    def get_success_url(self):
        return reverse('home')

    def get_context_data(self, **kwargs):

            context = super(ProfileUpdateView, self).get_context_data(**kwargs)
            context['action'] = reverse('profiles:update',
                                        kwargs={'pk': self.get_object().id})

            return context
