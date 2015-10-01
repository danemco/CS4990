from django.conf.urls import url

from django.views.generic import TemplateView
from . import views

urlpatterns = [
   url(r'^$', views.SongListView.as_view(), name="songlist"),
   url(r'^add/$', views.AddSongView.as_view(), name="addsong"),
   url(r'^(?P<pk>[0-9]+)/detail/$', views.SongDetailView.as_view(), name="songdetail"),
   url(r'^(?P<pk>[0-9]+)/$', views.SongUpdateView.as_view(), name="songupdate"),
   url(r'^(?P<pk>[0-9]+)/delete/$', views.SongDeleteView.as_view(), name="deletesong"),
   url(r'^del/success$', TemplateView.as_view(template_name="form3/success.html"), name="delsongsuccess"),
]
