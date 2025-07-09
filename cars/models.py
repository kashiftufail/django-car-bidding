# cars/models.py
from django.db import models
from autoslug import AutoSlugField
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.urls import reverse
from images.models import Image
from accounts.models import UserProfile


def validate_title_length(value):
    if len(value) > 200:
        raise ValidationError("Title cannot exceed 200 characters.")

class Car(models.Model):
    title = models.CharField(
        max_length=200,
        unique=True,
        validators=[
            MinLengthValidator(10, message="Title must be at least 10 characters."),
            validate_title_length
        ],
        error_messages={
            "unique": "This title already exists. Please use a different one.",
            "blank": "Title cannot be blank."
        }
    )
    detail = models.TextField()
    slug = AutoSlugField(populate_from="title", unique=True)
    seller = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="cars")

    def get_absolute_url(self):
        return reverse("cars:car_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title
