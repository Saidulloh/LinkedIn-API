from rest_framework import serializers

from apps.wallets.models import Wallet


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        read_only_fields = ('owner', )
        fields = (
            'id',
            'amount',
            'created_at'
        )
