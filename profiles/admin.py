# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import Profile

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile, ProfileAdmin)
