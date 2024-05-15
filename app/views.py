from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from .models import Post
from django.urls import reverse_lazy


class PostListView(ListView):
    model = Post
    template_name = 'list.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'detail.html'


class PostUpdateView(UpdateView):
    model = Post
    fields = ('title', 'image', 'video', 'voice')
    template_name = 'update.html'
    success_url = reverse_lazy('posts')


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('posts')


class PostCreateView(CreateView):
    model = Post
    fields = ('title', 'image', 'video', 'voice')
    template_name = 'create.html'
    success_url = reverse_lazy('posts')
