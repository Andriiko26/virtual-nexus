from django.urls import path
from .views import ProfileView, ProfileDetailView

urlpatterns = [
    path('', ProfileView.as_view(), name='profile'),
    path('<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),
]
