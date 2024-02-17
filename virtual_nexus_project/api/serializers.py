from rest_framework import serializers
from posts.models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields  = ['id','title', 'body', 'tags']

class CommentListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = ['text', 'author', 'created_at']