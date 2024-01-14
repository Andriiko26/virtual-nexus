from django.shortcuts import render, get_object_or_404, redirect
from django.views import View 
from .models import Post
from .forms import PostForm

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

class CreatePostView(View):
    template_name = 'posts/post_create.html'
    form_class = PostForm

    def get(self, request):
        form = self.form_class()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post-home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)