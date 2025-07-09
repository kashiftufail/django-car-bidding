from django.db import models
# from posts.models import Post
from django.apps import apps

from django.contrib.auth import get_user_model

User = get_user_model()

def image_upload_path(instance, filename):
    """Uploads to media/<user_id>/<filename>."""
    return f"uploads/{instance.uploaded_by_id}/{filename}"

class Image(models.Model):
    file        = models.ImageField(upload_to=image_upload_path)
    alt_text    = models.CharField(max_length=255, blank=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="uploaded_images")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey( "posts.Post",
        on_delete=models.CASCADE,
        related_name="images",
        null=True,  # Allow null initially to support existing data
        blank=True
    )

    car = models.ForeignKey('cars.Car', 
        null=True, blank=True, 
        on_delete=models.SET_NULL, 
        related_name='images'
    )

    def __str__(self):
        return self.alt_text or f"Image {self.pk}"
