from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Profile, Post

# Create your views here.
class ListAllPosts(ListView):
    model = Post
    paginate_by = 10
    queryset = Post.objects.all().order_by('-pub_date')

class ProfileDetailView(DetailView):
    model = Profile
