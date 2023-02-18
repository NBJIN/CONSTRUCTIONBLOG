from .models import Post, Comment
# from .models import Category
from django import forms
from ckeditor.fields import RichTextField
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

# choices = Category.objects.all().values_list('cat_name', 'cat_name')
# choice_list = []

# for item in choices:
#     choice_list.append(item)
# form models


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
        fields = ['author', 'added', 'mainbody']
        labels = {
            # 'Post': 'Name of Post:',
            'author': 'Author of Comment:',
            # 'cat_name': 'Category',
            'added': 'Date of Comment',
            'mainbody': 'Content',
                  }
        widgets = {
            # 'post': forms.TextInput,
           'author': forms.TextInput(attrs={'class': 'form-control'}),
            # 'cat_name': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            # 'added': forms.DateInput(format='%d/%m/%Y', attrs={'class': 'form-control'}),
            'added': forms.DateInput(format='%Y/%m/%d', attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
            'mainbody': forms.Textarea(attrs={'class': 'form-control'})
        }
        success_message = "You have successfully added your comment.."
        # content = RichTextField(max_length=5000, blank=True, null=True)


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
        # content = RichTextField(max_length=5000, blank=True, null=True)


# class CategoryAdd(forms.ModelForm):
#     class Meta:
#         model = Category
#         fields = ['cat_name', 'slug']
#         labels = {
#             'cat_name': 'Category Name:',
#             'slug': 'Slug',

#                   }
#         widgets = {
#             'cat_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'slug': forms.SlugField(required=True)(attrs={'class': 'form-control'}),

#         }
#         success_message = "You have successfully updated your comment.."
#         # content = RichTextField(max_length=5000, blank=True, null=True)
