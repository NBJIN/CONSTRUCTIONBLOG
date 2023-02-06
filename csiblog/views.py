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
    # fields = (
    # name = models.CharField(max_length=200, unique=True)
    # slug = models.SlugField(max_length=200)
    # contributor = models.ForeignKey(
    #     User, on_delete=models.CASCADE, related_name="csiblog_posts")
    # date = models.DateTimeField(auto_created=True)
    # image = CloudinaryField('image', default='placeholder')
    # content = RichTextField(max_length=5000, blank=True, null=True)
    # no_of_likes = models.ManyToManyField(
    #     User, related_name="csiblog_no_of_likes")
    # excerpt = models.TextField()

    # )
