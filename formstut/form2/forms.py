from django import forms

class BookForm(forms.Form):
    title = forms.CharField()
    author = forms.CharField()
    pages = forms.IntegerField()

