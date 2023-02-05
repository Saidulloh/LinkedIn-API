from django.db import models
from django.contrib.auth import get_user_model

from apps.contacts.models import Contact


User = get_user_model()


class ContactAppend(models.Model):
    """
    Model for adding contacts in contact table
    """
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='contact_append_owner',
        verbose_name='contact_append_owner'
    )
    contact = models.ForeignKey(
        Contact,
        on_delete=models.CASCADE,
        related_name='contact',
        verbose_name='contact'
    )
    members = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='contact_members',
        verbose_name='contact_members'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='created_at'
    )

    def __str__(self):
        return f'{self.id} -- {self.contact}'

    class Meta:
        verbose_name = 'contact append'
        verbose_name_plural = 'Contact appends'
