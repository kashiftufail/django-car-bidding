from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from cars.models import Car
from .models import Bid
from .tasks import send_bid_notification_to_seller

@login_required
def place_or_update_bid(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    price = request.POST.get("price")
    message = request.POST.get("message", "")

    bid, created = Bid.objects.update_or_create(
        car=car,
        user=request.user,
        defaults={"price": price, "message": message},
    )

    if created:
        email = getattr(getattr(car.seller, 'user', None), 'email', None)
        if email:
            try:
                send_bid_notification_to_seller.delay(
                    car.title, email, request.user.username, price, message
                )
            except Exception as e:
                print(f"Notification error: {e}")
    else:
        print("Bid updated, no notification sent.")

    return redirect(car.get_absolute_url())
