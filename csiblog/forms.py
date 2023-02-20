from .models import Post, Comment
from django import forms
from ckeditor.fields import RichTextField
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        
        fields = ['name', 'slug', 'contributor', 'date', 'image', 'content', 'no_of_likes']
        
        labels = {
            'name': 'Name of Post:',
            'slug': 'Slug:',
            'contributor': 'Author of Post:',
            # 'cat_name': 'Category',
            'date': 'Date of Post',
            'image': 'Post Image',
            'content': 'Post Content',
            'no_of_like': 'Likes',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'contributor': forms.Select(attrs={'class': 'form-control'}),
            # 'cat_name': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            # 'date': forms.DateInput(format='%Y/%m/%d', attrs={'class': 'datepicker'}),
            'date': forms.DateInput(format='%Y/%m/%d', attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
            # 'date': forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'})),
            # 'image': forms.ImageField,
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }
        
        success_message = "You have successfully added your post.."
        # content = RichTextField(max_length=5000, blank=True, null=True)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'added', 'mainbody',]
        labels = {
            'author': 'Author of Comment:',
            'added': 'Date of Comment',
            'mainbody': 'Content',
                  }
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your name'}),
            'added': forms.DateInput(format='%Y/%m/%d', attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
            'mainbody': forms.Textarea(attrs={'class': 'form-control'})
        }
        success_message = "You have successfully added your comment.."


class CommentUpdateForm(forms.ModelForm):
    class Meta:

        model = Comment
        fields = ['author', 'added', 'mainbody', 'approved']
        labels = {

            'author': 'Author of Comment:',
            # 'cat_name': 'Category',
            'added': 'Date of Comment',
            'mainbody': 'Content',
                  }

        widgets = {

            'author': forms.TextInput(attrs={'class': 'form-control'}),
            # 'cat_name': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            # 'added': forms.DateInput(format='%d/%m/%Y', attrs={'class': 'form-control'}),
            'added': forms.DateInput(format='%Y/%m/%d', attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
            'mainbody': forms.Textarea(attrs={'class': 'form-control'})
        }

        success_message = "You have successfully updated your comment.."
