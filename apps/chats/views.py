from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Q
from django.contrib.auth import get_user_model

from apps.chats.models import Chat
from apps.chats.serializers import ChatSerializer, ChatCreateSerializer
from apps.contacts.models import Contact


User = get_user_model()


class ChatApiViewSet(GenericViewSet,
                     ListModelMixin,
                     RetrieveModelMixin,
                     CreateModelMixin,
                     DestroyModelMixin):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        queryset = Chat.objects.filter(Q(members__in=[self.request.user]) | Q(owner=self.request.user))
        return queryset
    
    def destroy(self, request, *args, **kwargs):
        chat_id = kwargs['pk']
        chat = Chat.objects.get(id=chat_id)
        if chat.members.count() == 1:
            chat.delete()
        chat.members.remove(request.user)

    def get_serializer_class(self):
        if self.action == 'create':
            return ChatCreateSerializer
        return ChatSerializer

    def create(self, request, *args, **kwargs):
        chat_members = [int(i) for i in request.data['members']]
        try:
            contacts = Contact.objects.get(owner=request.user)
            for contact in contacts.members.all():
                if contact.id in chat_members:
                    return super().create(request, *args, **kwargs)
                return Response({'Error': 'You do not have in contact list any user!'})
        except:
            return Response({'Error': 'You do not have in contact list any user!'})
