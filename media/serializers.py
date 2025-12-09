from rest_framework import serializers
from .models import Comment, Post

class CommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    is_liked_by_user = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = '__all__'

    # Nested replies
    def get_replies(self, obj):
        return CommentSerializer(obj.replies.all(), many=True, context=self.context).data

    # Total likes for this comment
    def get_likes_count(self, obj):
        return obj.likepost.count()  # use the related_name from CommentLike model

    # Whether the current user liked this comment
    def get_is_liked_by_user(self, obj):
        request = self.context.get('request', None)
        if request and request.user.is_authenticated:
            return obj.likepost.filter(user=request.user).exists()
        return False
    
    class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)  # include all comments with likes and replies

    class Meta:
        model = Post
        fields = ['id', 'user', 'caption', 'created_at', 'comments']
        read_only_fields = ['user', 'created_at']





"""from rest_framework import serializers 
from .models import Comment,Post



class CommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()
    replies = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    likeuser = serializers.SerializerMethodField()
    #likes_count = serializers.IntegerField(source='likes.count', read_only=True)

    class Meta:
        model = Comment
        fields='__all__' 

    
    def get_replies(self, obj):
        return CommentSerializer(obj.replies.all(), many=True).data
    
class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)  # include comments
    class Meta:
        model = Post
        fields = ['id', 'user', 'caption', 'created_at', 'comments']
        read_only_fields = ['user', 'created_at']

    
    def get_likeuser(self, obj):
        user = self.context['request'].user"""

    

    
    