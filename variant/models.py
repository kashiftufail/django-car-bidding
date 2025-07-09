# variant/models.py

from django.db import models
from make.models import Make

class Variant(models.Model):
    make = models.ForeignKey(Make, on_delete=models.CASCADE, related_name="variants")
    name = models.CharField(max_length=100)

    class Meta:
        unique_together = ['make', 'name']  # Ensure each variant is unique per make
        ordering = ['make__name', 'name']
        verbose_name = "Car Variant"
        verbose_name_plural = "Car Variants"

    def __str__(self):
        return f"{self.make.name} {self.name}"
