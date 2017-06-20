from django.conf.urls import url

from views import DashboardView, ProgressFormView, ReportsView

urlpatterns = [
        url(r'^$', DashboardView.as_view(), name='dashboard'),
        url(r'^progress$', ProgressFormView.as_view(), name='progress'),
        url(r'^reports$', ReportsView.as_view(), name='reports'),
]
