from django.shortcuts import render
from django.views.generic import FormView # generic view for forms
from django.core.urlresolvers import reverse_lazy # helps us resolve URLs based on urls.py
from django.core.mail import send_mail # helper function for senidng email via Django

from .forms import ContactForm # our form

# Create your views here.
class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'form1/contact_form.html'
    success_url = reverse_lazy('form1:contactsuccess')

    def form_valid(self, form):
        # Send an email
        # send_mail(subject, message, from, [to], fail_silently)

        send_mail(form.cleaned_data['subject'], 
                  form.cleaned_data['message'], 
                  form.cleaned_data['from_email'], 
                  ['dpurcell@dixie.edu'],
                  fail_silently=False)
        return super(ContactFormView, self).form_valid(form)

    
