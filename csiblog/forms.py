from .models import Post, Comment
from django import forms
from ckeditor.fields import RichTextField
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    class Meta:
        model = Post

        fields = ['name',  'contributor', 'date', 'image', 'content', 'no_of_likes']
        # 'slug',
        labels = {
            'name': 'Name of Post:',
            # 'slug': 'Slug:',
            'contributor': 'Author of Post:',
            # 'cat_name': 'Category',
            'date': 'Date of Post',
            'image': 'Post Image',
            'content': 'Post Content',
            'no_of_like': 'Likes',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            # 'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'contributor': forms.Select(attrs={'class': 'form-control'}),
        #     # 'cat_name': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'date': forms.DateInput(format='%Y/%m/%d', attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
        #     # 'date': forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'})),
            # 'image': forms.ImageField,
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }

        success_message = "You have successfully added your post.."
        # content = RichTextField(max_length=5000, blank=True, null=True)


class CommentForm(forms.ModelForm):
    # author = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = Comment
        # fields = ['title', 'mainbody']
        fields = ['post', 'mainbody']
        # labels = {
        #     # 'post': 'Post',
        #     'title': 'Title',
        #     'mainbody': 'Content',
        #           }

        widgets = {
            # 'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your name'}),
            # 'author': forms.HiddenInput(),
            # 'added': forms.DateInput(format='%Y/%m/%d', attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
            # 'post': forms.HiddenInput(),
            # 'title': forms.TextInput(attrs={'class': 'form-control'}),
            # 'mainbody': forms.Textarea(attrs={'class': 'form-control'})
            'content': forms.Textarea(attrs={'rows': 4}),
        }
    #     success_message = "You have successfully added your comment.."

    def __init__(self, *args, **kwargs):
        post_id = kwargs.pop('post_id')
        # self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        self.fields['post'].initial = post_id
        self.fields['post'].widget = forms.HiddenInput()
        # self.fields['post'].widget = forms.HiddenInput()
        # self.fields['post'].initial = self.request.POST.get('post_id')
        # self.fields['author'].widget = forms.HiddenInput()
        # self.fields['author'].initial = self.request.user
        # self.fields['author'].initial = self.request.user.id if self.request.user.is_authenticated else None

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.request:
            instance.author = self.request.user
            # instance.post_id = self.request.POST.get('post_id')
        if self.post_id:
            instance.post_id = self.post_id
        if commit:
            instance.save()
        return instance
        # comment = super().save(commit=False)
        # comment.author = self.request.user
        # if commit:
        #     commit.save()
        # return comment

    def clean(self):
        cleaned_data = super().clean()
        if not self.instance.post_id:
            raise forms.ValidationError('This post field is required.')
        return cleaned_data

    def form_valid(self, form):
        form.instance.post_id = self.request.POST.get('post_id')
        return super().form_valid(form)


class CommentUpdate(forms.ModelForm):
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
