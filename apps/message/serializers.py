from rest_framework import serializers

from apps.message.models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        read_only_fields = ('owner', 'is_read',)
        fields = (
            'id',
            'text',
            'created_at',
            'updated_at',
            'chat',
        )


class MessageDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        read_only_fields = ('owner', 'is_read',)
        fields = (
            'id',
            'text',
            'created_at',
            'updated_at'
        )
