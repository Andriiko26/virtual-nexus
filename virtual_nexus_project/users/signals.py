from django.db.models.signals import post_save
from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from django.contrib.auth.models import User
from .models import UserProfile

@receiver(user_signed_up)
def create_user_profile(request, user):
    User.objects.create(user=user)