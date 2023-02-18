from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.views import generic, View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post, Comment
# from .models import Likes
# from .models import Category
# from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView
from .forms import PostForm, CommentForm, CommentUpdateForm
# from .forms import CategoryAdd
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

# # Create your views here.


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


class PostAddView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Post
    template_name = "postcreate.html"
    # fields = ['name', 'slug', 'contributor', 'date', 'image', 'content', 'no_of_likes', 'excerpt', 'status']
    form_class = PostForm
    login_url = 'postread'
    # permission_denied_message = 'You are not allowed access here please login'
    success_url = reverse_lazy('postread')
    success_message = "You have successfully added your post.."
    # queryset = Post.objects.filter(status=1).order_by('-date')

    def form_valid(self, form):
        form.instance.contributor = self.request.user
        return super().form_valid(form)


class PostUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
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
    login_url = 'postread'
    success_message = "You have successfully deleted your post.."
    success_url = reverse_lazy('postread')
    # success_url = "/"

    def test_func(self):
        return self.request.user == self.get_object().contributor


class PostView(ListView):
    model = Post
    template_name = "postread.html"


class PostDetailView(DetailView):
    model = Post
    template_name = "likes"
    success_url = reverse_lazy('postread.html')


# class LikesView(ListView):
#     def post(self, request, pk, *args, **kwargs):
#         post = Post.objects.get(pk=pk)

#         is_like = False

#         for like in post.likes.all():
#             if like == request.user:
#                 is_like = True

#                 break 

#             If not is.like:
#             post.likes.add(request.user)

#             if is_like:
#                 post.likes.remove(request.user)

#                 next = request.POST.get('next', '/')
#                 return HttpResponseRedirect(next)






#     model = Likes 
#     template_name = "likes"

#     def LikesView(request, pk):
#         post = get_object_or_404(Post, id=request.POST.get('post_id'))
#         post.likes.add(request.user)
#         success_url = reverse_lazy('likes', args=[str(pk)])




# class Likes(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
#     value = models.CharField(choices=LIKE_CHOICES, default='Likes', max_length=20)

#     def __str__(self):
#         return str(self.user) + ':' + str(self.post) +':' + str(self.value)

#     class Meta:
#        unique_together = ("user", "post", "value")

    # def get_success_url(self):
    #     return reverse("Likes", kwargs={"pk": self.kwargs.get("pk")})

    # def get(self, request, *args, **kwargs):
    #     like = Likes()
    #     like.post = get_object_or_404(Post, pk=self.kwargs.get("pk"))
    #     like.user = self.request.user
    #     like.save()
    #     return redirect(self.get_success_url())

    
    

class CommentView(CreateView):
    model = Comment
    # form_class = CommentForm
    template_name = "postdetail.html"
    success_url = reverse_lazy('postread.html')

    def likes(self, request, slug):
        likes = get_object_or_404(likes)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
            return HttpResponseRedirect(reverse('postdetail', args=[slug]))



class CommentAddView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Comment
    template_name = "commentadd.html"
    # fields = ['name', 'slug', 'contributor', 'date', 'image', 'content', 'no_of_likes', 'excerpt', 'status']
    form_class = CommentForm
    login_url = 'postread'
    # permission_denied_message = 'You are not allowed access here please login'
    success_url = reverse_lazy('postread')
    success_message = "You have successfully added your comment.."

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    # def form_valid(self, form):
    #     form.instance.contributor = self.request.user
    #     return super().form_valid(form)


    # def test_func(self):
    #     return self.request.user == self.get_object().contributor



class CommentUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Comment
    template_name = "postupdate.html"
    # fields = ('name', 'contributor', 'date', 'content',)
    form_class = PostForm
    # login_url = 'postread'
    success_message = "You have successfully updated your post.."
    success_url = reverse_lazy('postread')

    def test_func(self):
        return self.request.contributor == self.get_object().user


class CommentDelete(LoginRequiredMixin, SuccessMessageMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = "commentdelete"
    login_url = 'postread'
    success_message = "You have successfully deleted your comment.."
    success_url = reverse_lazy('postread')
    # success_url = "/"

    def test_func(self):
        return self.request.user == self.get_object().author


# class CategoryAdd(LoginRequiredMixin, SuccessMessageMixin, CreateView):
#     model = Category
#     template_name = "categoryadd.html"
#     # fields = ['name']
#     form_class = CategoryAdd
#     # login_url = 'postread'
#     # permission_denied_message = 'You are not allowed access here please login'
#     success_url = reverse_lazy('postread')
#     success_message = "You have successfully added your post.."
#     # queryset = Post.objects.filter(status=1).order_by('-date')


# class CategoryUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
#     model = Category
#     # template_name = 'postcreate.html', 'postupdate.html', 'postread.html', 'postdetail.html', 'postdelete.html', 'commentupdate.html', 'commentdelete.html',  'commentadd.html'
#     # # fields = ('name', 'contributor', 'date', 'content',)
#     form_class = CategoryAdd
#     # login_url = 'postread'
#     success_message = "You have successfully updated your post.."
#     success_url = reverse_lazy('postread')

#     def test_func(self):
#         return self.request.contributor == self.get_object().user


# class CategoryDelete(LoginRequiredMixin, SuccessMessageMixin, UserPassesTestMixin, DeleteView):
#     model = Category
#     # form_class = CategoryAdd
#     fields = ['name', 'slug']
#     template_name = "categorydelete.html"
#     success_message = "You have successfully Deleted this Category"
#     # success_url = "/"

#     def test_func(self):
#         return self.request.user == self.get_object().contributor


# class CategoryView(ListView):
#     model = Category
#     template_name = "categoryview.html"
#     form_class = CategoryAdd
