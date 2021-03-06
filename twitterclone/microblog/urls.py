from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
#   url(r'^$', login_required(views.IdeaListView.as_view()), name="idealist"),
    url(r'^$', views.ListAllPosts.as_view(), name="allposts"),
    url(r'^user/(?P<pk>\d+)/$', views.ProfileDetailView.as_view(), name="profiledetail"),
    url(r'^myfeed/$', login_required(views.MyFeedView.as_view()), name="myfeed"),
    url(r'^user/(?P<pk>\d+)/follow/$', login_required(views.FollowFormView.as_view()), name="follow"),
    url(r'^user/(?P<pk>\d+)/follow/success/$', login_required(views.FollowSuccessView.as_view()), name="followsuccess"),
]
