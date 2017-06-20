from django.conf.urls import url

from views import DashboardView, ProgressFormView, ReportsView

urlpatterns = [
        url(r'^$', DashboardView, name='dashboard'),
        url(r'^progress$', ProgressFormView, name='progress'),
        url(r'^reports$', ReportsView.as_view(), name='reports'),
]
