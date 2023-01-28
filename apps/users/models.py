from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

from utils.NumberValidator import phone_validator


class User(AbstractUser):
    """
    Model for user
    """
    username = models.CharField(
        unique=True,
        max_length=255,
        verbose_name='username'
    )
    avatarka = models.ImageField(
        upload_to='avatarka/',
        verbose_name='avatarka',
        null=True,
        blank=True
    )
    bio = models.TextField(
        verbose_name='bio',
        null=True,
        blank=True
    )
    email = models.EmailField(
        unique=True,
        verbose_name='email'
    )
    phone_number = models.CharField(
        max_length=13,
        validators=[phone_validator],
        verbose_name='phone_number'
    )
    created_at = models.DateTimeField( 
        auto_now_add=True,
        verbose_name='created_at'
    )
    age = models.IntegerField(
        verbose_name='age',
        null=True,
        blank=True
    )
    last_activity = models.DateTimeField(
        default=timezone.now(),
        verbose_name='last_activity'
    )

    def __str__(self):
        return f'{self.id} -- {self.username}'

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'Users'
