from rest_framework_simplejwt.views import TokenObtainPairView
from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView

urlpatterns = [
    path('', PostListView.as_view()),
    path('<uuid:pk>/', PostDetailView.as_view()),
    path('create/', PostCreateView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]