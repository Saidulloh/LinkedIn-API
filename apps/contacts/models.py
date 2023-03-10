from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Contact(models.Model):
    """
    Model for contacts
    """
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='contact_owner',
        verbose_name='contact_owner'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='created_at'
    )

    def __str__(self):
        return f'{self.id} -- {self.owner}'

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'Contacts'
