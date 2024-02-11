from markdownx.models import MarkdownxField
from django.db import models
from markdownx.utils import markdownify
from django.contrib.auth.models import User
from django.urls import reverse
import uuid

class Tag(models.Model):
    tag_text = models.CharField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        self.tag_text = self.tag_text.lower()
        super().save(*args, **kwargs)

class Post(models.Model):
    
    id = models.UUIDField(
        primary_key=True,
        default= uuid.uuid4,
        editable=False,
    )
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    body = MarkdownxField()
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
    
    @property
    def formatted_markdown(self):
        return markdownify(self.body)
    
    def get_absolute_url(self):
        return reverse('post-detail', args=(str(self.id),))
    

class Comment(models.Model):
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.author.username} - {self.text[:20]}'

class Like(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.user}: {self.post}'