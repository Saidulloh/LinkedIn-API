from rest_framework import serializers

from apps.contact_details.models import ContactAppend


class ContactAppendSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactAppend
        read_only_fields = ('owner', )
        fields = (
            'id',
            'contact',
            'created_at',
            'members'
        )
