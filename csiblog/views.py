from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic, View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from django import forms


# # Create your views here.


class PostView(ListView):
    model = Post
    template_name = "postread.html"
    success_url = reverse_lazy('postcreate.html')


class PostDetailView(DetailView):

    # def get(self, request, slug, *args, **kwargs):
    #     queryset = Post.objects.filter(status=1)
    #     post = get_object_or_404(queryset, slug=slug)
    model = Post
    template_name = "postdetail.html"
    success_url = reverse_lazy('postread.html')


class PostAddView(CreateView):
    model = Post
    template_name = "postcreate.html"
    fields = ('name', 'slug', 'contributor', 'date', 'image', 'content', 'excerpt', 'status')
    success_url = reverse_lazy('postread')

class PostUpdate(UpdateView):
    model = Post
    template_name = "postupdate.html"
    fields = ('name', 'date', 'content',)
    success_url = reverse_lazy('postread')


class PostDelete(DeleteView):
    model = Post
    template_name = "postdelete.html"
    success_url = reverse_lazy('postread')
