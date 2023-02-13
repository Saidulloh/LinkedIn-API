from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.users.models import WorkExperience, Skills, Education
from apps.posts.serializers import PostSerializer
from apps.favorites.serializers import FavoriteSerializer


User = get_user_model()

fields = ['id', 'username', 'avatarka', 'bio', 'email', 'created_at', 'phone_number', 'age', 'premium_active']



class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        read_only_fields = ('owner',)
        fields = (
            'id',
            'title',
            'from_date',
            'to_date',
            'description'
        )


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        read_only_fields = ('owner',)
        fields = (
            'id',
            'title',
            'from_date',
            'to_date',
            'description'
        )


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = fields + ['password', 'skill']

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
            'last_activity',
            'premium_active'
        )


class UserSerializer(serializers.ModelSerializer):
    owner = PostSerializer(read_only=True, many=True)
    favorite_owner = FavoriteSerializer(read_only=True, many=True)
    skill = SkillsSerializer(read_only=True, many=True)
    work_experience = WorkExperienceSerializer(read_only=True, many=True)
    education = EducationSerializer(read_only=True, many=True)

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
            'premium_active',
            'wallet',
            'password',
            'owner',
            'favorite_owner',
            'skill',
            'work_experience',
            'education'
        )
