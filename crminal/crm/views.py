from django.shortcuts import render
from django.views.generic import DetailView, TemplateView
from django.db.models import Count

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


        
