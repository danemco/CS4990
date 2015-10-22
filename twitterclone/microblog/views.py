from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, FormView, View 
from django.views.generic.detail import SingleObjectMixin
from django.core.urlresolvers import reverse_lazy, reverse
from django import forms

from .models import Profile, Post

# Create your views here.
class ListAllPosts(ListView):
    model = Post
    paginate_by = 10
    queryset = Post.objects.all().order_by('-pub_date')

class ProfileDetailView(DetailView):
    model = Profile

class MyFeedView(ListView):
    model = Post
    paginate_by = 10
    template_name = "microblog/myfeed.html"

    def get_queryset(self):
        my_profile = self.request.user.profile_set.all()[0]
        following_profile_list = list(my_profile.following.all())
        following_profile_list.append(my_profile)
        return Post.objects.filter(profile__in = following_profile_list)

class FollowFormView(SingleObjectMixin, View):
    model = Profile

    def post(self, request, *args, **kwargs):
        
        my_profile = request.user.profile_set.all()[0]
        my_profile.following.add(self.get_object())
        my_profile.save()
        #return HttpResponseRedirect(reverse('microblog:followsuccess', kwargs = {'pk': self.get_object().pk}))
        #if request.is_ajax():
        #    return Http
        return HttpResponseRedirect(reverse('microblog:followsuccess', args = (self.get_object().pk, )))

class FollowSuccessView(SingleObjectMixin, TemplateView):
    template_name = 'microblog/follow_success.html'
    model = Profile







# class FollowFormView(FormView):
#     success_url = reverse_lazy('microblog:followsuccess')
# 
#     class FollowUserForm(forms.Form):
#         follow_user_id = forms.IntegerField(widget=forms.HiddenInput)
# 
#     form_class = FollowUserForm
# 
#     def form_valid(self, form):
#         self.user_id
#         
