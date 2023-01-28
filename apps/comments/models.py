from django.db import models
from django.contrib.auth import get_user_model

from apps.posts.models import Post


User = get_user_model()


class Comment(models.Model):
    """
    Model for comments
    """
    content = models.CharField(
        max_length=256,
        verbose_name='content'
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='children',
        verbose_name='children',
        null=True,
        blank=True
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='comments_owner',
        verbose_name='comments_owner'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments_post',
        verbose_name='comments_post'
    )

    def __str__(self):
        return f'{self.id} -- {self.owner} -- {self.post}'

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'Comments'
