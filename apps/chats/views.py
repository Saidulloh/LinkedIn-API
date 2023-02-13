from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from django.contrib.auth import get_user_model

from apps.chats.models import Chat
from apps.chats.serializers import ChatSerializer, ChatCreateSerializer
from apps.contact_details.models import ContactAppend


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
        queryset = Chat.objects.filter(Q(members__in=[self.request.user]) | Q(owner=self.request.user)) # filter chats
        return queryset
    
    def destroy(self, request, *args, **kwargs):
        chat_id = kwargs['pk']
        chat = Chat.objects.get(id=chat_id)
        if chat.members.count() == 1: # if count of chat member == 1
            chat.delete()
        if request.user in chat.members.all(): # if user is a member of chat
            chat.members.remove(request.user) # delete user of this chat
        chat.owner = None

    def get_serializer_class(self):
        if self.action == 'create':
            return ChatCreateSerializer
        return ChatSerializer

    def create(self, request, *args, **kwargs):
        try:
            chat_members = [int(i) for i in request.data['members'] if request.user != i] # get chat members
            contacts = ContactAppend.objects.filter(owner=request.user) # get my contacts
            contact_members = [int(i.members.id) for i in contacts] # list of contact members id
            if set(chat_members).issubset(contact_members): # check have users in contact list
                return super().create(request, *args, **kwargs)
            else:
                return Response({'Error': 'You do not have in contact list any user!'})
        except Exception as ex:
            print(ex)
            return Response(ex)
