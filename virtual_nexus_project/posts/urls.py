from django.urls import path
from .views import (
    PostsListView, 
    PostDetailView, 
    CreatePostView,
    PostSearch,
    PostLike,
    PostEditView,
    PostDeleteView,
)

urlpatterns = [
    path('', PostsListView.as_view(), name='post-home'),
    path('<uuid:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('create_post/', CreatePostView.as_view(), name='post-create'),
    path('search/', PostSearch.as_view(), name='post-search'),
    path('<uuid:pk>/like/', PostLike.as_view(), name='post-like'),
    path('<uuid:pk>/edit/', PostEditView.as_view(), name='post-edit'),
    path('<uuid:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]