from django.shortcuts import render
from django.views.generic import DetailView, TemplateView, ListView
from django.db.models import Count, Q
from viewsets import ModelViewSet

from django.contrib.auth.models import User
from .models import Opportunity, Contact, Reminder, Report, Stage, CallLog, Campaign, Company, OpportunityStage

# Create your views here.
class DashboardView(TemplateView):
    template_name = 'crm/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['opportunity_list'] = Opportunity.objects.all().order_by('-create_date')[:5]
        context['reminder_list'] = Reminder.objects.all().exclude(completed = True).order_by('date')[:5]
        context['stage_list'] = User.objects.annotate(num_opp = Count('opportunity'))
        context['stage_by_opp_list'] = Stage.objects.annotate(opp_count = Count('opportunity'))

        return context


        
class OpportunityView(ListView):
    model = Opportunity

class OpportunityDetailView(DetailView):
    model = Opportunity

class SearchResultsView(TemplateView):
    template_name = 'crm/search_results.html'

    def get_context_data(self, **kwargs):
        context = super(SearchResultsView, self).get_context_data(**kwargs)

        # If we don't have a search term in the URL, just return the context as is.
        # Otherwise, populate the template context with potential search results.
        if not self.request.GET.get("q", None):
            return context

        term = self.request.GET["q"]
        context['searchterm'] = term
        context["opportunity_list"] = Opportunity.objects.filter(name__icontains = term)

        return context

