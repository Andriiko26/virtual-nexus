from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView

urlpatterns = [
    path('', PostListView.as_view()),
    path('<uuid:pk>/', PostDetailView.as_view()),
    path('create/', PostCreateView.as_view()),
]