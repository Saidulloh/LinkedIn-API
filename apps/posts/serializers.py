from rest_framework import serializers

from apps.posts.models import Post
from apps.comments.models import Comment
from apps.comments.serializers import CommentSerializer
from apps.likes.models import PostLike
from apps.likes.serializers import PostLikeSerializer


class PostSerializer(serializers.ModelSerializer):
    comment_count = serializers.SerializerMethodField(read_only=True)
    like_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        read_only_fields = ('owner',)
        fields = (
            'id',
            'title',
            'image',
            'description',
            'created_at',
            'comment_count',
            'like_count'
        )
    
    def get_comment_count(self, obj):
        comments = Comment.objects.filter(post=obj.id)
        return comments.count()
    
    def get_like_count(self, obj):
        likes = PostLike.objects.filter(post=obj.id)
        return likes.count()


class PostDetailSerializer(serializers.ModelSerializer):
    posts = serializers.SerializerMethodField(read_only=True)
    likes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        read_only_fields = ('owner',)
        fields = (
            'id',
            'title',
            'image',
            'description',
            'created_at',
            'updated_at',
            'posts',
            'likes'
        )

    def get_posts(self, obj):
        comments = Comment.objects.filter(post=obj.id)
        serializer = CommentSerializer(comments, many=True)
        return serializer.data


    def get_likes(self, obj):
        comments = PostLike.objects.filter(post=obj.id)
        serializer = PostLikeSerializer(comments, many=True)
        return serializer.data