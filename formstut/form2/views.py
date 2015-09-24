from django.shortcuts import render
from django.views.generic import ListView, FormView # generic view for forms
from django.core.urlresolvers import reverse_lazy # helps us resolve URLs based on urls.py

from .forms import BookForm # our form
from .models import Book

# Create your views here.

class BookListView(ListView):
    model = Book

    def get_context_data(self, *args, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context["form"] = BookForm
        return context
        

class AddBookView(FormView):
    form_class = BookForm
    template_name = 'form2/addbook_form.html'
    success_url = reverse_lazy('form2:addbooksuccess')

    def form_valid(self, form):
        # Add a book
        book = Book()
        book.title = form.cleaned_data['title']
        book.author = form.cleaned_data['author']
        book.pages = form.cleaned_data['pages']
        book.save()

        return super(AddBookView, self).form_valid(form)

    
