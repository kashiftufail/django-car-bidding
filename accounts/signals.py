from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile
from accounts.thread_locals import get_signup_role, clear_signup_role



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = UserProfile.objects.create(user=instance)
        role = get_signup_role()
        if role:
            profile.role = role
            profile.save()
        clear_signup_role()
