from django.contrib import admin
from .models import Post, Comment, Category


admin.site.register(Post)


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug', 'contributor', 'date', 'status')
    list_filter = ('name', 'contributor', 'date',  'status')
    search_fields = ('name', 'content')
    date_hierarchy = 'date'


admin.site.register(Comment)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'mainbody', 'added', 'approved')
    list_filter = ('title', 'added', 'mainbody', 'added',  'approved')
    search_fields = ('title', 'added')
    date_hierarchy = 'added'
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'name')
    list_filter = ('name', 'name')
    search_fields = ('name', 'name')