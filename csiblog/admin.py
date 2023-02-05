from django.contrib import admin
# added code below
from .models import Post, Comment


# Register your models here.
# @admin.register(Post)
# class PostAdmin
admin.site.register(Post)
admin.site.register(Comment)
