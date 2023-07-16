from .models import Post, Comment
from django import forms
from ckeditor.fields import RichTextField
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.models import User

import datetime


class PostForm(forms.ModelForm):
    class Meta:
        model = Post

        # fields = ['name',  'contributor', 'date', 'image', 'content', 'no_of_likes']
        
        fields = ['name','date', 'image', 'content']
        # 'slug',
        labels = {
            'name': 'Post Name:',
            # 'slug': 'Slug:',
            # 'contributor': 'Author of Post:',
            # 'cat_name': 'Category',
            'date': 'Post Date:',
            'image': 'Post Image:',
            'content': 'Post Content:',
            # 'no_of_like': 'Likes',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            # 'slug': forms.TextInput(attrs={'class': 'form-control'}),
            # 'contributor': forms.Select(attrs={'class': 'form-control'}),
        #     # 'cat_name': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            # 'date': forms.DateField(widget=forms.DateInput(format='%Y/%m/%d', attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'})),
            'date': forms.DateInput(format='%Y/%m/%d', attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
        # # 'date': forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'})),
            # 'image': forms.ImageField(),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }

        # success_message = "You have successfully added your post.."
        # content = RichTextField(max_length=5000, blank=True, null=True)

    # def __init__(self, *args, **kwargs):
    #     form = PostForm(request=request)
    #     self.request = kwargs.pop('request')
    #     contributor = kwargs.pop('contributor')

    #     super().__init__(*args, **kwargs)
    #     self.contributor = contributor 

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
            return instance 

    # def save(self, commit, request):
    #     post_form = PostForm(data=request.POST)
    #     if post_form.is_valid():
    #         post_form.instance.contributor = rquest.user.username
    #         post = post_form.save(commit=False)
    #         post.post = post
    #         post.save()
    #     else:
    #         post_form = PostForm()

    #     return render(
    #         request,
    #         "postdetail.html",
    #         {
    #             "name": name,
    #             "post": post,
    #             "post_form": PostForm,
    #         }
    #     )
        # instance = super().save(commit=False)
        # instance.author = self.request.user
        # instance.contributor = self.contributor
        # if commit:
        #     instance.save()
        # return instance

    def clean_name(self):
        name = self.cleaned_data.get('name')
        existing_post = Post.objects.filter(name=name).first()
        if existing_post and existing_post.slug != self.instance.slug:
            raise forms.ValidationError('Error please enter a new post name as this has been assigned a post already.')
        return name


class CommentForm(forms.ModelForm):
   
    class Meta:
        model = Comment
    
        fields = ['mainbody']
    

        widgets = {
         
            'added': forms.DateField(widget=forms.DateInput(format='%Y/%m/%d', attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'})),
        
            'mainbody': forms.Textarea(attrs={'rows': 4}),
        }
  

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        post_id = kwargs.pop('post_id')
       
        super().__init__(*args, **kwargs)
       
        self.post_id = post_id

    def save(self, commit=True):
        instance = super().save(commit=False)
     
        instance.author = self.request.user
   
        instance.post_id = self.post_id

        if commit:
            instance.save()
        return instance


    def clean(self):
        cleaned_data = super().clean()
      
        if not self.post_id:
            raise forms.ValidationError('This post field is required.')
        return cleaned_data

