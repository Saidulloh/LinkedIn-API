from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, \
    DestroyModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response

from apps.posts.models import Post
from apps.posts.serializers import PostSerializer, PostDetailSerializer
from utils.permissions import IsOwner


class PostApiViewSet(GenericViewSet,
                     ListModelMixin,
                     CreateModelMixin,
                     RetrieveModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    @action(
        detail=False, permission_classes=[IsAuthenticated], methods=['get']
    )
    def my_posts(self, request):
        posts = Post.objects.filter(owner=request.user)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostDetailApiViewSet(GenericViewSet,
                           UpdateModelMixin,
                           DestroyModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = [IsOwner]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
