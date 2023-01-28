from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.posts.serializers import PostSerializer
from apps.favorites.serializers import FavoriteSerializer


User = get_user_model()

fields = ['id', 'username', 'avatarka', 'bio', 'email', 'created_at', 'phone_number', 'age']


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = fields + ['password']

    def create(self, validated_data):
        password = validated_data['password']
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'avatarka',
            'last_activity'
        )


class UserSerializer(serializers.ModelSerializer):
    owner = PostSerializer(read_only=True, many=True)
    favorite_owner = FavoriteSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'avatarka',
            'bio',
            'email',
            'phone_number',
            'age',
            'last_activity',
            'password',
            'owner',
            'favorite_owner'
        )
