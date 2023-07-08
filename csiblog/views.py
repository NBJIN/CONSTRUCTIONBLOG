from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic, View
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
from .forms import PostForm, CommentForm, CommentUpdate
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


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

    # def form_valid(self, form):
    #     form.instance.contributor = self.request.user
    #     return super().form_valid(form)

    # def get(self, request):
    #     return render(request, 'postread.html')

    # def post(self, request):
    #     messages.success(request, 'Success')
    #     return render(request, 'postread.html')

    # def postaddview(reqeust):
    #     if request.method == 'POST':
    #         form = PostForm(request.POST)
    #         if form.is_valid():
    #             Post = form.save()
    #             return redirect('postdetail', slug=post.slug)
    #     else:
    #         form = PostForm()
    #     return render(request, 'postread.html', {'form': form})


class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = "postupdate.html"
    # fields = ('name', 'contributor', 'date', 'content',)
    form_class = PostForm
    # login_url = 'postread'
    success_message = "You have successfully updated your post.."
    success_url = reverse_lazy('postread')

    # # test for SuccessMessageMixin
    # def test_func(self):
    #     post = self.get_object()
    #     if self.request.user == post.contributor:
    #         return True
    #     return False

    def test_func(self):
        return self.request.contributor == self.get_object().user

    # def form_valid(self, form):
    #     form.instance.contributor = self.request.user
    #     return super().form_valid(form)


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
    # # paginate_by = 4


class PostDetailView(DetailView):
    model = Post
    template_name = "postdetail.html"
    success_url = reverse_lazy('postread.html')

    def get_context_data(self, **kwargs):
        # like = get_object_or_404(Post, id=self.kwargs['pk'])
        # post_like = like.post_like()
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['no_of_likes'] = post.no_of_likes
        return context


    # def get(self, reqeust, slug, *args, **kwargs):
    #     queryset = Post.objects.filter(status=1)
    #     post = get_object_or_404(queryset, slug=slug)
    #     comments = post.comments.filter(approved=True).order_by('created_on')
    #     liked = False
    #     if post.likes.filter(id=self.request.user.id).exists():
    #         liked = True

    #         return render(
    #             request,
    #             "posdetail.html",
    #             {
    #                 "post": post,
    #                 "comments": comments,
    #                 "liked": liked
    #             },
    # )


class Display(TemplateView):
    model = Comment
    form_class = CommentForm
    template_name = "display.html"
    success_url = reverse_lazy('postread.html')


def CommentView(id):
    comment = Comment.queryset.get(id=id)
    comment.view()

    # def likes(self, request, slug):
    #     likes = get_object_or_404(likes)

    #     if post.likes.filter(id=request.user.id).exists():
    #         post.likes.remove(request.user)
    #     else:
    #         post.likes.add(request.user)
    #         return HttpResponseRedirect(reverse('postdetail', args=[slug]))


# def CommentAddView(id):
#     comment = Comment.queryset.get(id=id)
#     comment.addview()


class CommentAddView(CreateView):
    model = Comment
    template_name = "commentadd.html"
#     # fields = ['name', 'slug', 'contributor', 'date', 'image', 'content', 'no_of_likes', 'excerpt', 'status']
    form_class = CommentForm
#     login_url = 'postread'
#     # permission_denied_message = 'You are not allowed access here please login'
#     success_url = reverse_lazy('postread')
#     success_message = "You have successfully added your comment.."
# class CommentAddView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
#     model = Comment
#     template_name = "commentadd.html"
#     # fields = ['name', 'slug', 'contributor', 'date', 'image', 'content', 'no_of_likes', 'excerpt', 'status']
#     form_class = CommentForm
#     login_url = 'postread'
#     # permission_denied_message = 'You are not allowed access here please login'
#     success_url = reverse_lazy('postread')
#     success_message = "You have successfully added your comment.."

#     def form_valid(self, form):
#         form.instance.post_id = self.kwargs['pk']
#         return super().form_valid(form)

# class CommentUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
#     model = Comment
#     template_name = "commentupdate.html"
#     form_class = CommentUpdate
#     # login_url = 'postread'
#     # success_message = "You have successfully updated your post.."
#     success_url = reverse_lazy('postdetail')

#     def form_valid(self, form):
#         form.instance.comment_id = self.kwargs['pk']
#         return super().form.valid


class CommentUpdate(UpdateView):
    model = Comment
    template_name = "commentupdate.html"
    form_class = CommentUpdate
    # login_url = 'postread'
    # success_message = "You have successfully updated your post.."


def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)

    success_url = reverse_lazy('postdetail', kwargs={'pk': self.object.post.pk})


# def CommentUpdate(id):
#     comment = Comment.queryset.get(id=id)
#     comment.update()


class CommentDelete(DetailView):
    model = Comment
    template_name = "commentdelete.html"
    # form_class = CommentUpdate
    # login_url = 'postread'
    # success_message = "You have successfully updated your post.."
    success_url = reverse_lazy('postdetail')


def PostlikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_like'))
    post.no_of_likes.add(request.user)
    return HttpResponseRedirect(reverse('postdetail', args=[str(pk)]))


# def CommentDelete(id):
#     comment = Comment.queryset.get(id=id)
#     comment.delete()
