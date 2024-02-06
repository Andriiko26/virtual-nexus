from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from posts.models import Post
from .serializers import PostSerializer

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