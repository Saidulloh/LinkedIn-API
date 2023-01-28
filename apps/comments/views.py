from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, ListModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAuthenticated

from apps.comments.models import Comment
from apps.comments.serializers import CommentSerializer, CommentCreateSerializer


class CommentApiViewSet(GenericViewSet,
                        ListModelMixin,
                        CreateModelMixin,
                        DestroyModelMixin,
                        UpdateModelMixin):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Comment.objects.filter(owner=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return CommentSerializer
        return CommentCreateSerializer
