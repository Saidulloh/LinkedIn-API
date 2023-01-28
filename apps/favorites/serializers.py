from rest_framework import serializers

from apps.favorites.models import Favorite
from apps.posts.serializers import PostSerializer


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        read_only_fields = ('owner',)
        fields = (
            'id',
            'post'
        )


class FavoriteRetrieveSerializer(serializers.ModelSerializer):
    post = PostSerializer(read_only=True)

    class Meta:
        model = Favorite
        read_only_fields = ('owner',)
        fields = (
            'id',
            'post'
        )
