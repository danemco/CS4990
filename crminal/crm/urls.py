from django.contrib.auth.decorators import login_required
from django.conf.urls import url, patterns, include
from . import views

urlpatterns = [
   url(r'^$', login_required(views.DashboardView.as_view()), name="dashboard"),
   url(r'^opportunities/$', login_required(views.OpportunityView.as_view()), name="opportunity_list"),
   url(r'^opportunity/(?P<pk>\d+)/$', login_required(views.OpportunityDetailView.as_view()), name="opportunity_detail"),
   url(r'^search/$', login_required(views.SearchResultsView.as_view()), name="search"),
   # url(r'^report/$', login_required(views.ReportView.as_view()), name="report"),
]




