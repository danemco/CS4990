from django.forms.models import model_to_dict
from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from .models import Song
# Create your views here.
class AjaxableResponseMixin(object):
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = model_to_dict(self.object)
            return JsonResponse(data)
        else:
            return response


class SongListView(ListView):
    model = Song
    fields = ['title', 'musician', 'genre']

class SongDetailView(DetailView):
    model = Song

    def render_to_response(self, context, **kwargs):
        if self.request.is_ajax():
            return JsonResponse(serializers.serialize('json', self.object))
        return super(SongDetailView, self).render_to_response(context, **kwargs)

class AddSongView(CreateView):
    model = Song
    fields = ['title', 'musician', 'genre']
    success_url = reverse_lazy('form3:songlist')

class SongUpdateView(AjaxableResponseMixin, UpdateView):
    model = Song
    fields = ['title', 'musician', 'genre']
    success_url = reverse_lazy('form3:songlist')

class SongDeleteView(DeleteView):
    model = Song
    success_url = reverse_lazy('form3:delsongsuccess')

