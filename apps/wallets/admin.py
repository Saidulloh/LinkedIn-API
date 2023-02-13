from django.contrib import admin

from apps.wallets.models import Wallet


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
   list_display = ('id', 'owner', 'amount', 'created_at')
