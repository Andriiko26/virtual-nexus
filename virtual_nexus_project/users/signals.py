from django.db.models.signals import post_save
from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from django.contrib.auth.models import User
from .models import UserProfile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):

    if created and not UserProfile.objects.filter(user=instance).exists():
        UserProfile.objects.create(user=instance)

@receiver(user_signed_up)
def create_user_profile_after_signup(request, user, **kwargs):
    
    if not UserProfile.objects.filter(user=user).exists():
        UserProfile.objects.create(user=user)
