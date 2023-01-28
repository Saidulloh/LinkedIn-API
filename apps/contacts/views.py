from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticated

from apps.contacts.models import Contact
from apps.contacts.serializers import ContactSerializer
from utils.permissions import IsOwner


class ContactApiViewSet(GenericViewSet,
                        CreateModelMixin,
                        ListModelMixin,
                        RetrieveModelMixin,
                        DestroyModelMixin):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        queryset = Contact.objects.filter(owner=self.request.user)
        return queryset
