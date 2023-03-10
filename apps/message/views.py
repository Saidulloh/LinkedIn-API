from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticated

from apps.chats.models import Chat
from apps.message.models import Message
from apps.message.serializers import MessageSerializer, MessageDetailSerializer
from utils.permissions import IsOwner


class MessageApiViewSet(GenericViewSet,
                        CreateModelMixin):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def create(self, request, *args, **kwargs):
        try:
            owner = request.user
            chat_obj = Chat.objects.get(id=request.data['chat'])
            if owner in chat_obj.members.all() or owner == chat_obj.owner:
                Message.objects.create(text=request.data['text'], chat=chat_obj, owner=owner)
                return super().create(request, *args, **kwargs)
            return Response(data={"error": "You are not a member in chat {}".format(chat_obj.title)})
        except Chat.DoesNotExist:
            return Response(data={"error": "This chat does not exist"})


class MessageListDetailApiViewSet(GenericViewSet,
                                  ListModelMixin,
                                  UpdateModelMixin,
                                  DestroyModelMixin):
    queryset = Message.objects.all()
    serializer_class = MessageDetailSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        return Message.objects.filter(owner=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return MessageSerializer
        return MessageDetailSerializer
