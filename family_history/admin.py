# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import FamilyHistoryStats, FamilyName

class FamilyHistoryStatsAdmin(admin.ModelAdmin):
    pass

admin.site.register(FamilyHistoryStats, FamilyHistoryStatsAdmin)

class FamilyNameAdmin(admin.ModelAdmin):
    pass

admin.site.register(FamilyName, FamilyNameAdmin)
