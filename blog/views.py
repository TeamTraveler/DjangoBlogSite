from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Category


# Create your views here.
class PostList(ListView):
    model = Post
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all() 
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context
    

class PostDetail(DetailView):
    model = Post