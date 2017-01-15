from django.contrib import admin

from .models import Post


class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'updated', 'created',]
    # list_display_links = ['updated']
    # list_editable = ['title',]
    list_filter = ['title', 'updated']
    search_fields = ['title', 'content']

    class Meta:
        model = Post
# Register your models here.
admin.site.register(Post, PostModelAdmin)
