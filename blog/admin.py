from django.contrib import admin
from . models import Blog, Comment

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'publish_date', 'author',]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['blog', 'author', 'created_at']