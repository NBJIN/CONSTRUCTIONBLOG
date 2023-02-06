from django.shortcuts import render
# , get_object_or_404
from django.http import HttpResponse
from django.views import generic
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.urls import reverse_lazy
from .models import Post


class PostView(ListView):
    model = Post
    template_name = "postread.html"


class PostDetailView(DetailView):
    model = Post
    template_name = "postdetail.html"


# class PostAddView(AddView):
#     model = Post
#     template_name = "postadd.html"

# # Create your views here.
