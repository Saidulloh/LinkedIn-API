from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.favorites.models import Favorite
from apps.favorites.serializers import FavoriteSerializer, FavoriteRetrieveSerializer
from apps.posts.models import Post


class FavoriteApiViewSet(GenericViewSet,
                         CreateModelMixin,
                         DestroyModelMixin,
                         ListModelMixin,
                         RetrieveModelMixin):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Favorite.objects.filter(owner=self.request.user)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return FavoriteRetrieveSerializer
        return FavoriteSerializer

    def create(self, request, *args, **kwargs):
        post = Post.objects.get(id=request.data['post'])
        favorites = Favorite.objects.filter(post=post)
        for favorite in favorites:
            if favorite.owner == request.user:
                return Response({'Error': 'Have you already saved this post!'})
        return super().create(request, *args, **kwargs)
