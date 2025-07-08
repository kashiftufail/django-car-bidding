from django.conf import settings
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model
from images.models import Image
from roles.models import Role
from django.contrib.auth import get_user_model
User = get_user_model()


digits_only = RegexValidator(r"^\d+$", "Enter numbers only.")


def avatar_upload_path(instance, filename):
    return f"uploads/avatars/{instance.user_id}/{filename}"


class UserProfile(models.Model):

    user   = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)

    city   = models.CharField(max_length=120, blank=True)
    state  = models.CharField(max_length=120, blank=True)
    zip    = models.CharField(max_length=20, blank=True)
    avatar = models.OneToOneField(          # ← enforces 1‑to‑1
        Image,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="profile_avatar"
    )




    # keep blank=True so the row can be inserted without values
    phone = models.CharField(max_length=20, blank=True, validators=[digits_only])
    info  = models.TextField(blank=True)
    city  = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    zip   = models.CharField(max_length=20, blank=True)
    
    def clean(self):
        """
        Enforce phone / city / state / zip only after the profile exists.
        .clean() is called by ModelForms and admin automatically.
        """
        super().clean()

        # self.pk is None for an *unsaved* instance (signal’s .create() phase)
        if self.pk:
            missing = {}
            if not self.phone:
                missing["phone"] = "Phone number is required."
            if not self.city:
                missing["city"] = "City is required."
            if not self.state:
                missing["state"] = "State is required."
            if not self.zip:
                missing["zip"] = "ZIP code is required."

            if missing:
                # raise one ValidationError containing field-specific errors
                raise ValidationError(missing)


    def __str__(self):
        return f"Profile for {self.user.username}"
