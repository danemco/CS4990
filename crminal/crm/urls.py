from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from . import views

urlpatterns = [
   url(r'^$', login_required(views.DashboardView.as_view()), name="dashboard"),
   # url(r'^report/$', login_required(views.ReportView.as_view()), name="report"),
]
