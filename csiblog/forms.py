from .models import Post
from django import forms
from ckeditor.fields import RichTextField


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

        # content = RichTextField(max_length=5000, blank=True, null=True)
