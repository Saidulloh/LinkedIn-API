from rest_framework import serializers

from apps.contacts.models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        read_only_fields = ('owner',)
        fields = (
            'id',
            'members',
            'created_at',
            'updated_at'
        )
