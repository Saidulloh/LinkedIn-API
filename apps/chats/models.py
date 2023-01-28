from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Chat(models.Model):
    """
    Model for chats
    """
    title = models.TextField(
        verbose_name='title'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='created_at'
    )
    image = models.ImageField(
        upload_to='chat images/',
        verbose_name='chat_images'
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='chat_owner',
        verbose_name='chat_owner'
    )
    members = models.ManyToManyField(
        User,
        related_name='members',
        verbose_name='members'
    )

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = 'chat'
        verbose_name_plural = 'Chats'
