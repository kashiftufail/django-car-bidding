from django.db import models

class Make(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Car Make"
        verbose_name_plural = "Car Makes"
        ordering = ["name"]

    def __str__(self):
        return self.name
