from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import FormView, ListView
from django.utils import timezone
from .forms import PunchInForm, PunchOutForm
import datetime

from django.contrib.auth.models import User
from .models import Punch, Project

# Create your views here.
class ClockInOutView(FormView):
    success_url = reverse_lazy('timeclock:ko')

    def get_template_names(self):
        template_name = 'timeclock/home_clockin.html'
        records = self.request.user.punch_set.order_by('-time_in')
        print records
        if records:
            print "we have records."
            if records[0].is_clocked_in():
                print "record zero says we're clocked in"
                template_name = 'timeclock/home_clockout.html'
            else:
                print "record zero says we're NOT clocked in"
                

        return [template_name]
        

    def get_form_class(self):
        records = self.request.user.punch_set.order_by('-time_in')
        if records:
            if records[0].is_clocked_in():
                return PunchOutForm

        return PunchInForm

    def get_context_data(self, **kwargs):
        context = super(ClockInOutView, self).get_context_data(**kwargs)
        # Find the most recent punch and send that to the template context so we can do a count down timer
        objects = Punch.objects.filter(user = self.request.user).order_by('-time_in')

        if objects:
            context["last_punch"] = objects[0]
        else:
            context["last_punch"] = None
        return context

    def form_valid(self, form):
        if type(form).__name__ == 'PunchInForm':
            entry = Punch()
            entry.project = form.cleaned_data["project"]
            entry.user = self.request.user
            entry.save()

        if type(form).__name__ == 'PunchOutForm':
            entry = self.request.user.punch_set.order_by('-time_in')[0]
            entry.note = form.cleaned_data["note"]
            entry.time_out = timezone.now()
            entry.save()

        return super(ClockInOutView, self).form_valid(form)

class ReportView(ListView):
    model = Punch
    paginate_by = 2

    def get_queryset(self):
        queryset = Punch.objects.filter(user = self.request.user)        

        # except super users can see everyone
        if self.request.user.is_superuser:
            queryset = Punch.objects.all()        

        # if Project was in the querystring
        if self.request.user.is_superuser and "user" in self.request.GET and self.request.GET["user"] != "":
            queryset = queryset.filter(user = self.request.GET.get("user"))

        if "project" in self.request.GET and self.request.GET["project"] != "":
            queryset = queryset.filter(project = self.request.GET.get("project"))

        if "time_in" in self.request.GET and self.request.GET["time_in"] != "":
            queryset = queryset.filter(time_in__gte = self.request.GET.get("time_in"))
            
        if "time_out" in self.request.GET and self.request.GET["time_out"] != "":
            d = datetime.datetime.strptime(self.request.GET.get("time_out"), "%Y-%m-%d") 
            d = d + datetime.timedelta(days = 1)
            queryset = queryset.filter(time_in__lte = d)
            
        if "note" in self.request.GET and self.request.GET["note"] != "":
            queryset = queryset.filter(note__icontains = self.request.GET.get("note"))

        return queryset.order_by('-time_in')
            
    def get_context_data(self, **kwargs):
        context = super(ReportView, self).get_context_data(**kwargs)

        # Add all projects to the template's context
        context["projects"] = Project.objects.all().order_by('title')
        context["users"] = User.objects.all().order_by('first_name').order_by('username')

        # Get all objects for the current query
        queryset = self.get_queryset()

        # Commented out because this was a fun academic exercize
        #get_total_time = lambda queryset: sum([punch.duration() for punch in queryset])
        #context["total_time"] = get_total_time(queryset)

        total_time = datetime.timedelta(0)
        for punch in queryset:
            total_time += punch.duration()

        context["total_time"] = total_time

        return context

