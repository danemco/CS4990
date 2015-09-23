from django import forms

class ContactForm(forms.Form):
    name = forms.CharField()
    subject = forms.CharField()
    from_email = forms.CharField(widget=forms.EmailInput)
    message = forms.CharField(widget=forms.Textarea)

