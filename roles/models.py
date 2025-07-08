from django.db import models

# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=20, unique=True)  # seller, bidder, guest

    def __str__(self):
        return self.name
