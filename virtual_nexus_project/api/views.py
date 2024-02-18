from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from posts.models import Post, Like, Comment
from .serializers import PostSerializer, CommentListSerializer, CommentCreateSerializer, PostSearchSerializer
from django.contrib.auth import get_user_model

def get_user_id(request):
    """Accepts a request and returns the user id with the token in this request 
    """
    raw_token = request.headers.get('Authorization').split(' ')[1]
    decode_token = AccessToken(token=raw_token)
    return decode_token['user_id']


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
    """It should returned like counter and if the method is POST update counter
    *only registrated users can use it
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, *args, **kwargs):

        post = get_object_or_404(Post, pk=pk)
        post.likes_count = post.like_set.count()

        return Response({'likes_count': post.likes_count})

    def post(self, request, pk, *args, **kwargs):

        user = get_object_or_404(get_user_model(), id=get_user_id(request))
        post = get_object_or_404(Post, id=pk)
        like, created = Like.objects.get_or_create(user=user, post=post)

        if not created:
            like.delete()

        post.likes_count = post.like_set.count()
        post.save()
        return Response({'likes_count': post.likes_count}, status=status.HTTP_200_OK)
    
class PostCommentListView(APIView):
    """ return list of comments to this post
    """


    def get(self, request, pk, *args, **kwargs):

        post = get_object_or_404(Post, pk=pk)
        
        comments = Comment.objects.filter(post=post)
        serializer = CommentListSerializer(comments, many=True)
        return Response(serializer.data)

class PostCommentCreateView(APIView):
    """Create comments
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, pk, *args, **kwargs):

        post = get_object_or_404(Post, pk=pk)
        
        if not post:
            return Response({"detail": "Post does not exist."}, status=status.HTTP_404_NOT_FOUND)

        serializer = CommentCreateSerializer(data=request.data, context={'post': post})

        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class PostSearchView(APIView):
    """Return post by query
    *It's only searching by title
    """
    def get(self, request, *args, **kwargs):

        serializer = PostSearchSerializer(data=request.query_params)

        if serializer.is_valid():

            query = serializer.validated_data['query']
            posts = Post.objects.filter(title__icontains=query)
            posts_serializer = PostSerializer(posts, many=True)

            return Response(posts_serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)