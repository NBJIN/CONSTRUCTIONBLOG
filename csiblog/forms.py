from .models import Post, Comment
from django import forms
from ckeditor.fields import RichTextField
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


# form models
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'slug', 'contributor', 'date', 'image', 'content', 'no_of_likes']

        labels = {
            'name': 'Name of Post:',
            'slug': 'Slug:',
            'contributor': 'Author of Post:',
            'date': 'Date of Post',
            'image': 'Post Image',
            'content': 'Post Content',
            'no_of_like': 'Likes',

        }

        widgets = {

            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'contributor': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(format='%d/%m/%Y', attrs={'class': 'form-control'}),
            # 'image': forms.ImageField,
            'content': forms.Textarea(attrs={'class': 'form-control'})

        }
        success_message = "You have successfully added your post.."
        # content = RichTextField(max_length=5000, blank=True, null=True)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'added', 'mainbody']
        labels = {
            'Post': 'Name of Post:',
            'author': 'Author of Comment:',
            'added': 'Date of Comment',
            'mainbody': 'Content',
                  }
        widgets = {
            'post': forms.TextInput,
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'added': forms.DateInput(format='%d/%m/%Y', attrs={'class': 'form-control'}),
            'mainbody': forms.Textarea(attrs={'class': 'form-control'})
        }
        success_message = "You have successfully added your comment.."
        # content = RichTextField(max_length=5000, blank=True, null=True)


class CommentUpdateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['post', 'title', 'author', 'added', 'mainbody', 'approved']
        labels = {
            'Post': 'Name of Post:',
            'title': 'Title of Post',
            'author': 'Author of Comment:',
            'added': 'Date of Comment',
            'mainbody': 'Content',
            
                  }
        widgets = {
            'post': forms.TextInput,
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'added': forms.DateInput(format='%d/%m/%Y', attrs={'class': 'form-control'}),
            'mainbody': forms.Textarea(attrs={'class': 'form-control'})
        }
        success_message = "You have successfully updated your comment.."
        # content = RichTextField(max_length=5000, blank=True, null=True)
