from django.conf.urls import url

from . import views

urlpatterns = [
   url(r'^$', views.IndexView.as_view(), name="index"),
   url(r'^(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name="detail"),
   url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryDetailView.as_view(), name="categorydetail"),
]
