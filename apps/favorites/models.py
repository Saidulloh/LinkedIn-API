from django.db import models
from django.contrib.auth import get_user_model

from apps.posts.models import Post


User = get_user_model()


class Favorite(models.Model):
    """
    Model for favorite posts
    """
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorite_owner',
        verbose_name='favorite_owner'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='favorite_post',
        verbose_name='favorite_post'
    )

    def __str__(self):
        return f'{self.id} -- {self.post} -- {self.owner}'

    class Meta:
        verbose_name = 'favorite'
        verbose_name_plural = 'Favorites'
