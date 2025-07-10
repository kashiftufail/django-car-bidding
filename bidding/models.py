from django.db import models
from django.conf import settings
from cars.models import Car

class Bid(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='bids')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bids')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('car', 'user')  # Each user can only bid once per car

    def __str__(self):
        return f"Bid by {self.user.username} on {self.car.title}"
