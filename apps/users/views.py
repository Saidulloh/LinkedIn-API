from django.contrib.auth import get_user_model
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, ListModelMixin
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from apps.users.models import WorkExperience, Education
from apps.users.serializers import UserCreateSerializer, UserSerializer, UserListSerializer, WorkExperienceSerializer, EducationSerializer
from apps.users.permissions import IsOwner
from apps.contacts.models import Contact


User = get_user_model()


class UserCreateApiViewSet(GenericViewSet,
                           CreateModelMixin,
                           ListModelMixin):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return UserListSerializer
        return UserCreateSerializer
    
    @action(
        detail=False, permission_classes=[IsAuthenticated], methods=["get"]
    )
    def current_user(self, request, email=None):
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(
        detail=False, permission_classes=[IsAuthenticated], methods=["get"]
    )
    def another_users(self, request, email=None):
        lst = []
        contacts = Contact.objects.get(owner=request.user)
        for user in User.objects.all():
            if user in contacts.members.all() or user == request.user:
                continue
            lst.append(user)
        print(lst)
        users = User.objects.filter(id__in=[i.id for i in set(lst)])
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserApiViewSet(GenericViewSet,
                     RetrieveModelMixin,
                     UpdateModelMixin,
                     DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwner]

    def get_serializer_class(self):
        if self.action == 'get':
            return UserSerializer
        return UserCreateSerializer


class EducationApiViewSet(GenericViewSet,
                          CreateModelMixin,
                          UpdateModelMixin,
                          DestroyModelMixin):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class WorkExperienceApiViewSet(GenericViewSet,
                               CreateModelMixin,
                               UpdateModelMixin,
                               DestroyModelMixin):
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
