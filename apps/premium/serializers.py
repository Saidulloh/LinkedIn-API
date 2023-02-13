from rest_framework import serializers

from apps.premium.models import Premium, PremiumOrder


class PremiumSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Premium
        fields = (
            'id',
            'price',
            'date_during'
        )


class PremiumOrderSerializer(serializers.ModelSerializer):
    premium = PremiumSerialzer(read_only=True)
    
    class Meta:
        model = PremiumOrder
        read_only_fields = ('owner', )
        fields = (
            'id',
            'premium',
            'from_date',
            'is_active'
        )
