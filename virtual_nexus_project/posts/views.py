from django.shortcuts import render, get_object_or_404
from django.views import View 
from .models import Post

class PostsListView(View):
    template_name = 'posts/index.html'

    def get(self, request):
        posts = Post.objects.all()
        context={
            'posts':posts,
        }
        return render(request, self.template_name, context)

class PostDetailView(View):
    template_name = 'posts/post_detail.html'
    
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        context = {
            'post': post,
        }
        return render(request, self.template_name, context)
        