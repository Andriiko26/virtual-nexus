from django.urls import path
from .views import PostsListView, PostDetailView, CreatePostView

urlpatterns = [
    path('', PostsListView.as_view(), name='post-home'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('create_post/', CreatePostView.as_view(), name='post-create')
]