# posts/models.py
from django.db import models
from autoslug import AutoSlugField
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.urls import reverse
from images.models import Image


def validate_title_length(value):
    if len(value) > 200:
        raise ValidationError("Title cannot exceed 200 characters.")

class Post(models.Model):
    title = models.CharField(
        max_length=200,
        unique=True,
        validators=[
            MinLengthValidator(10, message="Title must be at least 10 characters."),
            validate_title_length  # Custom validator for max length message
        ],
        error_messages={
            "unique": "This title already exists. Please use a different one.",
            "blank": "Title cannot be blank.",
        }
    )
    body = models.TextField()
    slug = AutoSlugField(populate_from="title", unique=True)
    


    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title
