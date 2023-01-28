from django.contrib import admin

from apps.likes.models import PostLike#, CommentLike


class PostLikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'post')

admin.site.register(PostLike, PostLikeAdmin)


# class CommentLikeAdmin(admin.ModelAdmin):
#     list_display = ('id', 'owner', 'comment')

# admin.site.register(CommentLike, CommentLikeAdmin)
