from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class Blog_list(ListView):
    model = Post
    template_name = 'home.html'


class Blog_detail(DetailView):
    model = Post
    template_name = 'detail.html'
