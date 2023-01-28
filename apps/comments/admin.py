from django.contrib import admin

from apps.comments.models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'post', 'owner')

admin.site.register(Comment, CommentAdmin)
