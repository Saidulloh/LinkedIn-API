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
    skill = models.ManyToManyField(
        'Skills',
        verbose_name='skill'
    )
    premium_active = models.BooleanField(
        default=False,
        verbose_name='premium_active'
    )
    wallet = models.IntegerField(
        default=0,
        verbose_name='wallet'
    )

    def __str__(self):
        return f'{self.id} -- {self.username}'

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'Users'


class WorkExperience(models.Model):
    """
    Model for user work experience
    """
    title = models.CharField(
        max_length=256,
        verbose_name='title'
    )
    from_date = models.DateTimeField(
        verbose_name='from_date'
    )
    to_date = models.DateTimeField(
        verbose_name='to_date'
    )
    description = models.TextField(
        verbose_name='description'
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='work_experience',
        verbose_name='work_experience'
    )

    def __str__(self):
        return f'{self.id} -- {self.title}'

    class Meta:
        verbose_name = 'work experience'
        verbose_name_plural = 'Works experiences'


class Skills(models.Model):
    """
    Model for user skills
    """
    title = models.CharField(
        max_length=256,
        verbose_name='title'
    )

    def __str__(self):
        return f'{self.id} -- {self.title}'

    class Meta:
        verbose_name = 'skill'
        verbose_name_plural = 'Skills'


class Education(models.Model):
    """
    Model for education
    """
    title = models.CharField(
        max_length=256,
        verbose_name='title'
    )
    description = models.TextField(
        verbose_name='description'
    )
    from_date = models.DateTimeField(
        verbose_name='from_date'
    )
    to_date = models.DateTimeField(
        verbose_name='to_date'
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='education',
        verbose_name='education'
    )

    def __str__(self):
        return f'{self.id} -- {self.title}'

    class Meta:
        verbose_name = 'education'
        verbose_name_plural = 'Educations'
