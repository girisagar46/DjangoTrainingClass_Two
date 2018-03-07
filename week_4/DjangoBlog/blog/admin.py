import csv

from django.contrib import admin
from django.http import HttpResponse

from .models import Post, Comment

class ExportCSVMixin:
    def export_to_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment: filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response
    export_to_csv.short_description = "Export to CSV"


class PostAdmin(admin.ModelAdmin, ExportCSVMixin):
    list_display = ['title', 'author', 'created', 'status']
    search_fields = ['title', 'body']
    fields = ['title', 'body', 'author', 'status', 'publish']
    list_filter = ['status', 'created']
    # list_display_links = ['title', 'author']
    # list_editable = ['status']
    change_list_template = 'blog/change_list.html'

    actions = ['export_to_csv', 'abc']

    def abc(self, request, queryset):
        pass

    abc.short_description = "Thi sis ABC metgod"


class CommentAdmin(admin.ModelAdmin, ExportCSVMixin):
    list_display = ['name', 'post_id', 'email']
    actions = ['export_to_csv']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
