from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView
from .models import Idea, Profile, Category, Comment

# Create your views here.
class IdeaListView(ListView):
    model = Idea

class SecretView(TemplateView):
    template_name="kaizen/secret.html"

class CreateIdeaView(CreateView):
    model = Idea
    fields = ['title', 'description', 'category'] 

    def form_valid(self, form):
       idea = Idea()
       idea.profile     = Profile.objects.filter(user = self.request.user)[0]
       idea.title       = form.cleaned_data["title"]
       idea.description = form.cleaned_data["description"]
       idea.category    = form.cleaned_data["category"]
       idea.save()
       return super(CreateIdeaView, self).form_valid(form)

class ChangeStatusView(UpdateView):
    model = Idea
    fields = ['status']

