from .models import Post, Comment
from django import forms
from ckeditor.fields import RichTextField
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


# form models
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'slug', 'contributor', 'date', 'image', 'content', 'no_of_likes', 'excerpt', 'status']

        labels = {
            'name': 'Name of Post:',
            'slug': 'Slug:',
            'contributor': 'Author of Post:',
            'date': 'Date of Post',
            'image': 'Post Image',
            'content': 'Post Content',
            'no_of_like': 'Likes',
            'excerpt': 'Excerpt',
            'status': 'Status'
        }
        success_message = "You have successfully added your post.."
        # content = RichTextField(max_length=5000, blank=True, null=True)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['post', 'title', 'author', 'added', 'mainbody', 'approved']

        labels = {
            'post': 'Name of Post:',
            'title': 'Title of Comment:',
            'author': 'Author of Comment:',
            'added': 'Date of Comment',
            'mainbody': 'Content',
            'no_of_like': 'Likes',
                  }
        widgets = {
            'post': forms.TextInput,
            'title': forms.TextInput,
            'author': forms.TextInput,
            'added': forms.DateTimeField,
            'mainbody': forms.Textarea,
        }
        success_message = "You have successfully added your comment.."
        # content = RichTextField(max_length=5000, blank=True, null=True)
