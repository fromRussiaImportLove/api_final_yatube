from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Post, Comment, Group, Follow


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault(),
    )

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )
    post = serializers.SlugRelatedField(
        read_only=True,
        slug_field='id',
    )

    class Meta:
        fields = '__all__'
        model = Comment


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault())

    following = serializers.SlugRelatedField(
        queryset=Follow.following.get_queryset(),
        slug_field='username',
    )

    class Meta:
        fields = ('user', 'following')
        model = Follow
        validators = (UniqueTogetherValidator(
            queryset=Follow.objects.all(),
            fields=('user', 'following'),
            message='Your follow this author already.',
        ),)
