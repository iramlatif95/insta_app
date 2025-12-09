from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets,status 
from rest_framework.decorators import action 
from rest_framework.response import Response 
from.models import Comment 
from.serializers import CommentSerializer 
from rest_framework.pagination import PageNumberPagination
from .models import Comment, Likecomment, Post
from .serializers import PostSerializer
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication



# for the pagination
class CommentPagination(PageNumberPagination):
    page_size=10 

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class CommentViewSet(viewsets.ModelViewSet):
    serializer_class=CommentSerializer 
    pagination_class=CommentPagination

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        return Comment.objects.filter(post_id=post_id,parent=None).order_by('-created_at')
    
    # def perform_create(self, serializer):
    #     post=self.kwargs.get('post_id')
    #     parent_id=self.request.data.get('parent')
    #     parent_comment=Comment.objects.filter(id=parent_id).first() if parent_id else None
    #     serializer.save(user=self.request.user,post=post,parent=parent_comment)

    # like and like 
    

@action(detail=True, methods=['post'])
def like(self, request, post_id=None, pk=None):
    comment = get_object_or_404(Comment, id=pk)
    like, created = Likecomment.objects.get_or_create(comment=comment, user=request.user)

    if not created:
        # Already liked → unlike
        like.delete()
        return Response({
            'liked': False,  # instead of 'status': 'unliked'
            'likes_count': comment.likepost.count()
        })

    return Response({
        'liked': True,   # instead of 'status': 'liked'
        'likes_count': comment.likepost.count()
    })

        




    


# Create your views here.
