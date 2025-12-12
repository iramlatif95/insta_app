from rest_framework import serializers
from django.contrib.auth.models import User
from media.models import Post, Hashtag

class UserSearchSerializer(serializers.ModelSerializer):  # Capital S for convention
    class Meta:
        model = User
        fields = '__all__'

class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = ('id', 'name')

class PostSearchSerializer(serializers.ModelSerializer):
    user = UserSearchSerializer(read_only=True)  # optional: only if Post has a user FK
    tags = HashtagSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = '__all__'

