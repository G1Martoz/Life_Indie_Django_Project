from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

# vista basada en funciones


def posts(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})

# vista basada en clases


class PostListView(ListView):
    model = Post
    template_name = 'posts/posts.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/posts_individual.html'
    context_object_name = 'post'
    pk_url_kwarg = 'pk'
    queryset = Post.objects.all()
