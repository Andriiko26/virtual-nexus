from rest_framework.views import APIView
from rest_framework.response import Response
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
        