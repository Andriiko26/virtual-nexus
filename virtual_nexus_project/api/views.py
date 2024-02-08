from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from posts.models import Post, Like
from .serializers import PostSerializer
from django.contrib.auth import get_user_model

class PostListView(APIView):
    """Retruns all post data 
    """

    def get(self, request, *args, **kwargs):

        posts = Post.objects.all()
        serializer  = PostSerializer(posts, many=True)

        return Response(serializer.data, status.HTTP_200_OK)

class PostDetailView(APIView):

    def get(self, request, pk, *agrs, **kwargs):
        
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post)
        
        return Response(serializer.data, status.HTTP_200_OK)
    
    def put(self, request, pk, *args, **kwargs):
        
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, *args, **kwargs):
        
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class PostCreateView(APIView):


    def post(request, *args, **kwargs):

        serializer = PostSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)
    

class PostLikeView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, pk, *args, **kwargs):
        
        raw_token = request.headers.get('Authorization').split(' ')[1]
        decode_token = AccessToken(token=raw_token)
        user_id = decode_token['user_id']

        user = get_object_or_404(get_user_model(), id=user_id)

        post = get_object_or_404(Post, id=pk)
        like, created = Like.objects.get_or_create(user=user, post=post)

        if not created:
            like.delete()

        post.likes_count = post.like_set.count()
        post.save()
        return Response({'likes_count': post.likes_count}, status=status.HTTP_200_OK)
