from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created', 'status']
    search_fields = ['title', 'body']
    fields = ['title', 'body', 'author', 'status', 'publish']
    list_filter = ['status', 'created']
    # list_display_links = ['title', 'author']
    # list_editable = ['status']


admin.site.register(Post, PostAdmin)
