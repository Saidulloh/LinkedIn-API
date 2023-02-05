from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.contact_details.models import ContactAppend
from apps.contact_details.serializers import ContactAppendSerializer
from apps.contacts.models import Contact


class ContactAppendApiViewSet(GenericViewSet,
                              mixins.ListModelMixin,
                              mixins.CreateModelMixin,
                              mixins.UpdateModelMixin,
                              mixins.DestroyModelMixin):
    queryset = ContactAppend.objects.all()
    serializer_class = ContactAppendSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def create(self, request, *args, **kwargs):
        try:
            contact_obj = Contact.objects.get(id=request.data['contact'])
            if contact_obj.owner == request.user:
                contact_append_objs = ContactAppend.objects.filter(contact_id=contact_obj)
                if request.data['members'] == str(request.user.id):
                    return Response({"Error": "You can not add ur self!"})
                elif request.data['members'] in [str(contact_append_obj.members.id) for contact_append_obj in contact_append_objs]:
                    return Response({"Error": "This user is alredy taken!"})
                return super().create(request, *args, **kwargs)
            return Response({"Error": "you are not owner"})
        except Contact.DoesNotExist:
            return Response({"Error": "this contact list is not exist!"})
