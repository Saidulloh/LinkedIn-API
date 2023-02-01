from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.users.models import WorkExperience, Skills, Education
from apps.posts.serializers import PostSerializer
from apps.favorites.serializers import FavoriteSerializer


User = get_user_model()

fields = ['id', 'username', 'avatarka', 'bio', 'email', 'created_at', 'phone_number', 'age']



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
    work_experience = WorkExperienceSerializer(read_only=True) # Do not work
    education = EducationSerializer(read_only=True)            # Put request

    class Meta:
        model = User
        fields = fields + ['password', 'skill', 'work_experience', 'education']

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
    work_experience = WorkExperienceSerializer(read_only=True, many=True)
    education = EducationSerializer(read_only=True, many=True)
    skill = SkillsSerializer(read_only=True, many=True)

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
            'favorite_owner',
            'skill',
            'work_experience',
            'education'
        )
