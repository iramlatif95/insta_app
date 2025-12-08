from rest_framework import serializers 
from .models import Comment,Post



class CommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()
    likes_count = serializers.IntegerField(source='likes.count', read_only=True)

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
    

    
    