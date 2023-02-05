from django.contrib import admin
# added code below
from .models import Post, Comment


# Register your models here.
# @admin.register(Post)
# class PostAdmin


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug', 'contributor', 'date', 'revised', 'image', 'content', 'excerpt', 'status')
    list_filter = ('name', 'contributor', 'date', 'content', 'status')
    search_fields = ('name', 'content')
    raw_id_fields = ('contributor', 'no_of_likes')
    date_hierarchy = 'date'

# admin.site.register(Post)
# admin.site.register(Comment)
