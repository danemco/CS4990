from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from .models import Song
# Create your views here.

class SongListView(ListView):
    model = Song
    fields = ['title', 'musician', 'genre']

class AddSongView(CreateView):
    model = Song
    fields = ['title', 'musician', 'genre']
    success_url = reverse_lazy('form3:songlist')

class SongUpdateView(UpdateView):
    model = Song
    fields = ['title', 'musician', 'genre']
    success_url = reverse_lazy('form3:songlist')

class SongDeleteView(DeleteView):
    model = Song
    success_url = reverse_lazy('form3:delsongsuccess')

