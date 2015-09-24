from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.core.urlresolvers import reverse_lazy

from .models import Post, Comment, Category
from .forms import CommentForm

class IndexView(generic.ListView):
    template_name = 'blogapp/index.html'
    model = Post

    def get_queryset(self):
        #SELECT * from blogapp_post ORDER BY pub_date DESC LIMIT 5
        return Post.objects.order_by('-pub_date')[:5]


class PostDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView,self).get_context_data()
        context["form"] = CommentForm(initial={'post_id': self.object.pk})
        return context;

class PostCommentFormView(generic.detail.SingleObjectMixin, generic.FormView):
    form_class = CommentForm
    model = Post
    success_url = reverse_lazy('blogapp:comment_success')

    def form_valid(self, form):
        
        comment = Comment()
        comment.post = get_object_or_404(Post, pk=form.cleaned_data["post_id"])
        comment.person = form.cleaned_data["name"]
        comment.comment_text = form.cleaned_data["comment"]
        comment.save()
        return super(PostCommentFormView, self).form_valid(form)
    
class CategoryDetailView(generic.DetailView):
    model = Category
    # query set
