from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic, View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
# from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView
from .forms import PostForm


# # Create your views here.
class PostAddView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "postcreate.html"
    # fields = ['name', 'slug', 'contributor', 'date', 'image', 'content', 'no_of_likes', 'excerpt', 'status']
    form_class = PostForm
    login_url = 'postread'
    permission_denied_message = 'You are not allowed access here'
    success_url = reverse_lazy('postread')

    def form_valid(self, form):
        form.instance.contributor = self.request.user
        return super(PostAddView, self).form_valid(form)

# class PostUpdate(LoginRequiredMixin,  UserPassesTestMixin, UpdateView):


class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = "postupdate.html"
    # fields = ('name', 'contributor', 'date', 'content',)
    form_class = PostForm
    login_url = 'postread'
    success_url = reverse_lazy('postread')

    def test_func(self):
        return self.request.contributor == self.get_object().user


    # def test_func(self):
    #     self.object = self.get_object()
    #     return self.request.user == self.object.contributor


class PostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "postdelete.html"
    success_url = reverse_lazy('postread')

    def test_func(self):
        return self.request.user == self.get_object().user


class PostView(ListView):
    model = Post
    template_name = "postread.html"


class PostDetailView(DetailView):
    model = Post
    template_name = "postdetail.html"
    success_url = reverse_lazy('postread.html')
