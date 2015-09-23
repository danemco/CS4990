from django.conf.urls import url

from django.views.generic import TemplateView
from . import views

urlpatterns = [
   url(r'^contact/$', views.ContactFormView.as_view(), name="contactform"),
   url(r'^contact/success$', TemplateView.as_view(template_name="form1/success.html"), name="contactsuccess"),
]
