from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Post(models.Model):
    """
    Model for posts
    """
    title = models.CharField(
        max_length=256,
        verbose_name='title'
    )
    image = models.ImageField(
        upload_to='post_images/',
        verbose_name='image'
    )
    description = models.TextField(
        verbose_name='description'
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='owner',
        verbose_name='owner'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='created_at'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='updated_at'
    )

    def __str__(self):
        return f'{self.id} -- {self.title}'

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'Posts'
        ordering = ['created_at']
