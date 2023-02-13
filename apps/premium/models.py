from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Premium(models.Model):
    """
    Model for premium
    """
    price = models.IntegerField(
        verbose_name='price'
    )
    date_during = models.CharField(
        max_length=256,
        verbose_name='date during of days'
    )

    def __str__(self):
        return f'{self.id} -- {self.date_during}'

    class Meta:
        verbose_name = 'premium'
        verbose_name_plural = 'Premiums'


class PremiumOrder(models.Model):
    """
    Model for order premiums
    """
    premium = models.ForeignKey(
        Premium,
        on_delete=models.DO_NOTHING,
        related_name='premium_order',
        verbose_name='premium_order'
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='premium_owner',
        verbose_name='premium_owner'
    )
    from_date = models.DateField(
        auto_now_add=True,
        verbose_name='from_date'
    )
    is_active = models.BooleanField(
        default=False,
        verbose_name='is_active'
    )

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = 'premium order'
        verbose_name_plural = 'Premium orders'
