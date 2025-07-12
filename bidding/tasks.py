from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_bid_notification_to_seller(car_title, seller_email, bidder_name, bid_price, message):
    subject = f"New Bid on Your Car: {car_title}"
    body = (
        f"Hello,\n\nYou received a new bid on your car '{car_title}'.\n"
        f"Bidder: {bidder_name}\n"
        f"Price: ${bid_price}\n"
        f"Message: {message}\n\n"
        "Please log in to your dashboard to review the bid.\n\n"
        "Regards,\nBidCar Team"
    )

    send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [seller_email])
