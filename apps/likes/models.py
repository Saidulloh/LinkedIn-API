from django.db import models
from django.contrib.auth import get_user_model 

from apps.posts.models import Post
from apps.comments.models import Comment


User = get_user_model()


class PostLike(models.Model):
    """
    Model for post likes
    """
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='posts_likes',
        verbose_name='posts_likes'
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='owner_likes',
        verbose_name='owner_likes'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='created_at'
    )

    def __str__(self):
        return f'{self.id} -- {self.post.title}'

    class Meta:
        verbose_name = 'Post like'
        verbose_name_plural = 'Posts likes'


class CommentLike(models.Model):
    """
    Model for comment likes
    """
    owner = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='comment_likes_owner',
        verbose_name='comment_likes_owner'
    )
    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        related_name='comment_like',
        verbose_name='comment_like'
    )

    def __str__(self):
        return f'{self.id} -- {self.comment.title}'

    class Meta:
        verbose_name = 'comment like'
        verbose_name_plural = 'Comment likes'
