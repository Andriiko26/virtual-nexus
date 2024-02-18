from rest_framework_simplejwt.views import TokenObtainPairView
from django.urls import path
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView, 
    PostLikeView,
    PostCommentListView,
    PostCommentCreateView,
    PostSearchView
)

urlpatterns = [
    path('', PostListView.as_view()),
    path('<uuid:pk>/', PostDetailView.as_view()),
    path('create/', PostCreateView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('<uuid:pk>/like', PostLikeView.as_view()),
    path('<uuid:pk>/comments', PostCommentListView.as_view()),
    path('<uuid:pk>/comments/create', PostCommentCreateView.as_view()),
    path('search/', PostSearchView.as_view()),
]