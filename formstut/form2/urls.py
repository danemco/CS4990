from django.conf.urls import url

from django.views.generic import TemplateView
from . import views

urlpatterns = [
   url(r'^$', views.BookListView.as_view(), name="booklist"),
   url(r'^add/$', views.AddBookView.as_view(), name="addbook"),
   url(r'^add/success$', TemplateView.as_view(template_name="form2/success.html"), name="addbooksuccess"),
]
