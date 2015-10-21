from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from . import views

urlpatterns = [
#   url(r'^$', login_required(views.IdeaListView.as_view()), name="idealist"),
    url(r'^$', views.ListAllPosts.as_view(), name="allposts"),
    url(r'^user/(?P<pk>\d+)/$', views.ProfileDetailView.as_view(), name="profiledetail"),
]
