from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, HttpResponse
import datetime
from django.views import generic, View
from django.views.generic.edit import CreateView, FormMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy, reverse
from .models import Post, Comment
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.views.generic import TemplateView
from .forms import PostForm, CommentForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django import forms


class UserSignup(SuccessMessageMixin, CreateView):
    form_class = UserCreationForm
    template_name = "signup.html"
    success_url = reverse_lazy = "login.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    # success_message = "Your login was successful"


class UserLoginView(SuccessMessageMixin, CreateView):
    form_class = UserCreationForm
    template_name = "login.html"
    # success_url = "/success/"
    success_url = reverse_lazy = "postread.html"
    # success_message = "%(contributor)s was created successfully"

    def get(self, request):
        UserLoginView(request)
        return redirect('postread.html')
        messages.success(request, 'Your login was successfull.')


class UserLogoutView(CreateView):
    template_name = "logout.html"
    model = Post
    fields = ['contributor']


# class PostAddView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
class PostAddView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "postcreate.html"
    # fields = ['name', 'slug', 'contributor', 'date', 'image', 'content', 'no_of_likes', 'excerpt', 'status']
    form_class = PostForm
    login_url = 'postread.html'
    # permission_denied_message = 'You are not allowed access here please login'
    success_url = reverse_lazy('postread')
    success_message = "You have successfully added your post.."
    # queryset = Post.objects.filter(status=1).order_by('-date')

    def form_valid(self, form):
        form.instance.contributor = self.request.user
        return super().form_valid(form)


class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = "postupdate.html"
    # fields = ('name', 'contributor', 'date', 'content',)
    form_class = PostForm
    # login_url = 'postread'
    success_message = "You have successfully updated your post.."
    success_url = reverse_lazy('postread')


    def test_func(self):
        return self.request.contributor == self.get_object().user




class PostDelete(LoginRequiredMixin, SuccessMessageMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "postdelete.html"
    login_url = 'postread.html'
    success_message = "You have successfully deleted your post.."
    success_url = reverse_lazy('postread')
    # success_url = "/"

    def test_func(self):
        return self.request.user == self.get_object().contributor


class PostView(ListView):
    model = Post
    template_name = "postread.html"
    # queryset = Post.objects.filter(status=1).order_by('-date')
    paginate_by = 2


class PostDetailView(DetailView):
    model = Post
    template_name = "postdetail.html"
    success_url = reverse_lazy('postread.html')

    def get_context_data(self, **kwargs):
        # like = get_object_or_404(Post, id=self.kwargs['pk'])
        # post_like = like.post_like()
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['no_of_likes'] = post.no_of_likes.count()
        context['liked'] = post.no_of_likes.filter(id=self.request.user.id).exists()
        context['comments'] = post.csiblog_comment.all()
        return context

# class PostListView(ListView):
#     model = Post
#     template_name = "postread.html"
#     paginate_by = 3


def postread(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}


    return render(request, 'postread.html', context)




class Display(TemplateView):
    model = Comment
    form_class = CommentForm
    template_name = "display.html"
    success_url = reverse_lazy('postread.html')


def CommentView(id):
    comment = Comment.queryset.get(id=id)
    comment.view()


@login_required
def PostlikesView(request, pk):

    post = get_object_or_404(Post, pk=pk)
    liked = False
    if request.method == 'POST':
        if post.no_of_likes.filter(id=request.user.id).exists():
            post.no_of_likes.remove(request.user)
            liked = False
        else:
            post.no_of_likes.add(request.user)
            liked = True
    # total_no_of_likes = post.no_of_likes.count()
    return redirect('postdetail', pk=pk)




class CommentAddView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Comment
    template_name = "commentadd.html"
#     # fields = ['name', 'slug', 'contributor', 'date', 'image', 'content', 'no_of_likes', 'excerpt', 'status']
    form_class = CommentForm
    # fields = ['author', 'added', 'mainbody']
    success_url = reverse_lazy('postread')
    success_message = "You have successfully added your comment."

    def form_valid(self, form):
 
        form.instance.post_id = self.kwargs['pk']
        form.instance.author = self.request.user
        # form.request = self.request
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
     
        kwargs['post_id'] = self.kwargs['pk']
        kwargs['request'] = self.request
        return kwargs


    def get_success_url(self):
        return reverse_lazy('postdetail', kwargs={'pk': self.object.post.id})




def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)

    success_url = reverse_lazy('postdetail', kwargs={'pk': self.object.post.pk})


class CommentDelete(DeleteView):
    model = Comment
    template_name = "commentdelete.html"

    success_url = reverse_lazy('postdetail')

    def test_func(self):
        return self.request.user == self.get_object().contributor
