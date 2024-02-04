from django import forms
from .models import (
    Post,
    Comment,
    Tag,
)

class PostForm(forms.ModelForm):
    tags = forms.CharField(max_length=100, required=False)

    class Meta:
        model = Post
        fields = ['title', 'body', 'photo', 'tags']

    def clean_tags(self):
        raw_tags = self.cleaned_data['tags']
        tag_texts = [tag.strip().lower() for tag in raw_tags.split(',') if tag.strip()] 
        tags = [Tag.objects.get_or_create(tag_text=tag)[0] for tag in tag_texts]

        return tags

    def save(self, commit=True):
        post = super().save(commit=False)
        if commit:
            post.save()
            post.tags.set(self.cleaned_data['tags'])
        return post


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text']
