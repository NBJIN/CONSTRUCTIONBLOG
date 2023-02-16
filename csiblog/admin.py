from django.contrib import admin
# added code below
from .models import Post, Comment
# from .models import Category


# Register your models here.
# @admin.register(Post)
# class PostAdmin


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug', 'contributor', 'date', 'status')
    list_filter = ('name', 'contributor', 'date',  'status')
    search_fields = ('name', 'content')
    date_hierarchy = 'date'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'title', 'author', 'added', 'approved')
    list_filter = ('post', 'title', 'added',  'approved')
    search_fields = ('title', 'added')
    date_hierarchy = 'added'
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('catname', 'slug'),
#     prepopulated_fields = {'slug': ('cat_name',)}

#     def __str__(self):
#         return self.cat_name
