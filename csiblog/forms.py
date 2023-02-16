from .models import Post, Comment, Category
from django import forms
from ckeditor.fields import RichTextField
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

choices = Category.objects.all().values_list('catname', 'catname')
choice_list = [ ]

for item in choices:
    choice_list.append(item)
# form models
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'slug', 'contributor', 'catname', 'date', 'image', 'content', 'no_of_likes']

        labels = {
            'name': 'Name of Post:',
            'slug': 'Slug:',
            'contributor': 'Author of Post:',
            'catname': 'Category',
            'date': 'Date of Post',
            'image': 'Post Image',
            'content': 'Post Content',
            'no_of_like': 'Likes',

        }

        widgets = {

            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'contributor': forms.Select(attrs={'class': 'form-control'}),
            'catname': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'date': forms.DateInput(format='%d/%m/%Y', attrs={'class': 'form-control'}),
            # 'image': forms.ImageField,
            'content': forms.Textarea(attrs={'class': 'form-control'})

        }
        success_message = "You have successfully added your post.."
        # content = RichTextField(max_length=5000, blank=True, null=True)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'catname', 'added', 'mainbody']
        labels = {
            'Post': 'Name of Post:',
            'author': 'Author of Comment:',
            'catname': 'Category',
            'added': 'Date of Comment',
            'mainbody': 'Content',
                  }
        widgets = {
            'post': forms.TextInput,
            'author': forms.Select(attrs={'class': 'form-control'}),
            'catname': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'added': forms.DateInput(format='%d/%m/%Y', attrs={'class': 'form-control'}),
            'mainbody': forms.Textarea(attrs={'class': 'form-control'})
        }
        success_message = "You have successfully added your comment.."
        # content = RichTextField(max_length=5000, blank=True, null=True)


class CommentUpdateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['post', 'title', 'author', 'catname', 'added', 'mainbody', 'approved']
        labels = {
            'Post': 'Name of Post:',
            'title': 'Title of Post',
            'author': 'Author of Comment:',
            'catname': 'Category',
            'added': 'Date of Comment',
            'mainbody': 'Content',
            
                  }
        widgets = {
            'post': forms.TextInput,
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'catname': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'added': forms.DateInput(format='%d/%m/%Y', attrs={'class': 'form-control'}),
            'mainbody': forms.Textarea(attrs={'class': 'form-control'})
        }
        success_message = "You have successfully updated your comment.."
        # content = RichTextField(max_length=5000, blank=True, null=True)

class CategoryAdd(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['catname']
        labels = {
            'catname': 'Category Name:',

                  }
        widgets = {
            'catname': forms.TextInput(attrs={'class': 'form-control'}),

        }
        success_message = "You have successfully updated your comment.."
        # content = RichTextField(max_length=5000, blank=True, null=True)
