from django.contrib import admin

from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created', 'status']
    search_fields = ['title', 'body']
    fields = ['title', 'body', 'author', 'status', 'publish']
    list_filter = ['status', 'created']
    # list_display_links = ['title', 'author']
    # list_editable = ['status']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'post_id', 'email']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
