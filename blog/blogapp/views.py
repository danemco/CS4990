from django.shortcuts import render
from django.views import generic

from .models import Post, Comment, Category

class IndexView(generic.ListView):
    template_name = 'blogapp/index.html'
    model = Post

    def get_queryset(self):
        #SELECT * from blogapp_post ORDER BY pub_date DESC LIMIT 5
        return Post.objects.order_by('-pub_date')[:5]


class PostDetailView(generic.DetailView):
    model = Post

#     def get_context_data(self, *args, **kwargs):
#         context = super(PostDetailView,self).get_context_data()
#         context.update({"comment_list": self.get_object().comment_set.all()})
#        # context.update({"comment_list": Comment.objects.filter(post__pk = self.kwargs.get('pk'))})
#         return context;

class CategoryDetailView(generic.DetailView):
    model = Category
    # query set

















































# # Create your views here.
# class PostDetail(DetailView):
#     model = Post
# 
#     def get_context_data(self):
#         context = super(PostDetail,self).get_context_data()
#         context.update({"form": CommentForm()})
#         return context;
