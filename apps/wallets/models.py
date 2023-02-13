from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Wallet(models.Model):
    """
    Model for wallet
    """
    amount = models.IntegerField(
        default=0,
        verbose_name='amount'
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='wallet_owner',
        verbose_name='wallet_owner'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='created_at'
    )

    def __str__(self):
        return f'{self.id}'
    
    class Meta:
        verbose_name = 'wallet'
        verbose_name_plural = 'Wallets'
