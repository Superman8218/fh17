# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.views.generic import View

from account_conf import UPDATE_PROFILE_URL, LOGIN_TEMPLATE, REGISTRATION_TEMPLATE
from forms import RegistrationForm

from pudb import set_trace

def register_view(request):
    registration_template = REGISTRATION_TEMPLATE if REGISTRATION_TEMPLATE else 'accounts/register.html'

    form = RegistrationForm(data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        new_user = form.save()
        new_user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password1'],
                               )
        login(request, new_user)

        if UPDATE_PROFILE_URL:
            return HttpResponseRedirect(reverse(UPDATE_PROFILE_URL, kwargs={'pk':new_user.profile.pk}))
        else:
            return HttpResponseRedirect(reverse('home'))

    return render(request, registration_template, {
        'form': form
    })

class LoginView(View):
    def get(self, request):
        args = {}
        if 'next' in request.GET:
            args['next'] = request.GET['next']

        login_template = LOGIN_TEMPLATE if LOGIN_TEMPLATE else 'accounts/login.html'
        return render(request, login_template, args)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                if 'next' in request.POST:
                    redirectUrl = request.POST['next']
                else:
                    redirectUrl = reverse('home')
                return HttpResponseRedirect(redirectUrl)
            else:
                return HttpResponse("Your account is disabled")
        else:
            messages.add_message(self.request, messages.INFO, 'Invalid login')
            return HttpResponseRedirect(reverse('accounts:login'))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('accounts:login'))
