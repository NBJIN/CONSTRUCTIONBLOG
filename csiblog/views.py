from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic, View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
# from django import forms
from django.contrib.auth.mixins import (LoginRequiredMixin, UserPassesTestMixin)
from django.views.generic import TemplateView
from .forms import PostForm

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


class PostAddView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "postcreate.html"
    # fields = ['name', 'slug', 'contributor', 'date', 'image', 'content', 'no_of_likes', 'excerpt', 'status']
    form_class = PostForm
    success_url = reverse_lazy('postread')

    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super(PostAddView, self).form_valid(form)


class PostUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = "postupdate.html"
    fields = ('name', 'contributor', 'date', 'content',)
    form_class = PostForm
    success_url = reverse_lazy('postread')

    def get_object(self, queryset=None):
        if self.request.user.is_authenticated:
            queryset = Profile.objects.get(user=self.request.user)
        return queryset
    

    # def test_func(self):
    #     return self.request.user == self.get_object().user


class PostDelete(DeleteView):
    model = Post
    template_name = "postdelete.html"
    success_url = reverse_lazy('postread')
