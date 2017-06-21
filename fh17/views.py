from __future__ import unicode_literals

from django.db.models import Sum

from django.views.generic.base import TemplateView

from family_history.models import FamilyHistoryStats

class HomeView(TemplateView):
    template_name = 'fh17/home.html'

class ContactView(TemplateView):
    template_name = 'fh17/contact.html'

class ReportsView(TemplateView):
    template_name = 'fh17/reports.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ReportsView, self).get_context_data(*args, **kwargs)

        eq = FamilyHistoryStats.objects.filter(profile__group='EQ')
        if eq:
            context['eq_generations_total'] = 0 + int(eq.aggregate(Sum('generations'))['generations__sum'])
            context['eq_names_total'] = 0 + int(eq.aggregate(Sum('names'))['names__sum'])
            context['eq_indexed_total'] = 0 + int(eq.aggregate(Sum('indexed'))['indexed__sum'])
            context['eq_memories_total'] = 0 + int(eq.aggregate(Sum('memories'))['memories__sum'])
        else:
            context['eq_generations_total'] = 0
            context['eq_names_total'] = 0
            context['eq_indexed_total'] = 0
            context['eq_memories_total'] = 0

        rs = FamilyHistoryStats.objects.filter(profile__group='RS')
        if rs:
            context['rs_generations_total'] = 0 + int(rs.aggregate(Sum('generations'))['generations__sum'])
            context['rs_names_total'] = 0 + int(rs.aggregate(Sum('names'))['names__sum'])
            context['rs_indexed_total'] = 0 + int(rs.aggregate(Sum('indexed'))['indexed__sum'])
            context['rs_memories_total'] = 0 + int(rs.aggregate(Sum('memories'))['memories__sum'])
        else:
            context['rs_generations_total'] = 0
            context['rs_names_total'] = 0
            context['rs_indexed_total'] = 0
            context['rs_memories_total'] = 0

        return context
