from rest_framework import serializers

from apps.chats.models import Chat
from apps.users.serializers import UserListSerializer
from apps.message.models import Message
from apps.message.serializers import MessageDetailSerializer


class ChatSerializer(serializers.ModelSerializer):
    members = UserListSerializer(many=True, read_only=True)
    messages = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Chat
        read_only_fields = ('owner',)
        fields = (
            'id',
            'title',
            'created_at',
            'image',
            'members',
            'messages'
        )

    @staticmethod
    def get_messages(obj):
        messages_data = Message.objects.filter(chat_id=obj.id)
        serializer = MessageDetailSerializer(messages_data, many=True)
        return serializer.data


class ChatCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        read_only_fields = ('created_at', 'owner',)
        fields = (
            'title',
            'image',
            'members'
        )
