from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View 
from django.contrib import messages
from .models import Post
from .forms import PostForm


class PostsListView(View):
    """Return list of posts"""
    template_name = 'posts/index.html'
    posts_per_page = 3

    def get(self, request):
        post_list = Post.objects.all().order_by('-title')

        paginator = Paginator(post_list, self.posts_per_page)
        page = request.GET.get('page')

        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)  

        return render(request, self.template_name, {'posts':posts})


class PostDetailView(View):
    """Return detail of posts or 404"""

    template_name = 'posts/post_detail.html'
    
    def get(self, request, pk):

        post = get_object_or_404(Post, pk=pk)
        context = {
            'post': post,
        }
        return render(request, self.template_name, context)


class CreatePostView(View):
    """Create post class

    If the method is GET, it returns the post form. 
    If method is POST, it checks valid of data and add them to database 
    """
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
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post-home') 
        
        context = {
            'form': form
        }
        return render(request, self.template_name, context)