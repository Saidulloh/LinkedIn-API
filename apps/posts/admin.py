from django.contrib import admin

from apps.posts.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

admin.site.register(Post, PostAdmin)
