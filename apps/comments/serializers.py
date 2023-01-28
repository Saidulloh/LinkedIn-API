from rest_framework import serializers

from apps.comments.models import Comment
from apps.likes.models import CommentLike


class CommentSerializer(serializers.ModelSerializer):
    comment_likes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Comment
        read_only_fields = ('owner',)
        fields = (
            'id',
            'content',
            'parent',
            'post',
            'comment_likes'
        )

    @staticmethod
    def get_comment_likes(obj):
        from apps.likes.serializers import CommentLikeSerializer
        comment_like = CommentLike.objects.filter(comment=obj.id)
        serializer = CommentLikeSerializer(comment_like, many=True)
        return serializer.data


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        read_only_fields = ('owner',)
        fields = (
            'id',
            'content',
            'parent',
            'post'
        )
