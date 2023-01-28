from rest_framework import serializers

from apps.likes.models import PostLike, CommentLike


class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        read_only_fields = ('owner',)
        fields = (
            'id',
            'post',
        )


class CommentLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentLike
        read_only_fields = ('owner',)
        fields = (
            'id',
            'comment',
        )
