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
class CommentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['text']

    def create(self, validated_data):
        post = self.context.get('post')
        comment = Comment.objects.create(post=post, **validated_data)
        return comment

class PostSearchSerializer(serializers.Serializer):
    query = serializers.CharField()