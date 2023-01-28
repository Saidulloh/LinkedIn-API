from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

from apps.likes.models import PostLike, CommentLike
from apps.likes.serializers import PostLikeSerializer, CommentLikeSerializer
from apps.posts.models import Post
from apps.comments.models import Comment
from utils.permissions import IsOwner


class PostLikeApiViewSet(GenericViewSet,
                     CreateModelMixin,
                     DestroyModelMixin,
                     RetrieveModelMixin):
    queryset = PostLike.objects.all()
    serializer_class = PostLikeSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def create(self, request, *args, **kwargs):
        post = Post.objects.get(id=request.data['post'])
        likes = PostLike.objects.filter(post=post)
        for like in likes:
            if like.owner == request.user:
                return Response({'Error': 'Have you already liked this post!'})
        return super().create(request, *args, **kwargs)

    @action(
        detail=False, permission_classes=[IsOwner], methods=['get']
    )
    def my_likes(self, request):
        likes = PostLike.objects.filter(owner=request.user)
        serializer = PostLikeSerializer(likes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CommentLikeApiViewSet(GenericViewSet,
                            CreateModelMixin,
                            DestroyModelMixin,
                            RetrieveModelMixin):
    queryset = CommentLike.objects.all()
    serializer_class = CommentLikeSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def create(self, request, *args, **kwargs):
        comment = Comment.objects.get(id=request.data['comment'])
        likes = CommentLike.objects.filter(comment=comment)
        for like in likes:
            if like.owner == request.user:
                return Response({'Error': 'Have you already liked this comment!'})
        return super().create(request, *args, **kwargs)

    @action(
        detail=False, permission_classes=[IsOwner], methods=['get']
    )
    def my_likes(self, request):
        likes = CommentLike.objects.filter(owner=request.user)
        serializer = CommentLikeSerializer(likes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
