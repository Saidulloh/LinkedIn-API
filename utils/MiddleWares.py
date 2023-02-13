from django.utils import timezone
from django.contrib.auth import get_user_model

from apps.premium.models import Premium, PremiumOrder


User = get_user_model()


class IsActivePremiuMiddleWare:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        premium_order = PremiumOrder.objects.get(is_active=True, owner=request.user)  # get premium order
        premium = Premium.objects.get(id=premium_order.pk)  # get premium
        to_date = premium_order.from_date + timezone.timedelta(days=int(premium.date_during))  # end date
        user = User.objects.get(id=request.user.pk)
        response = self.get_response(request)
        if premium_order.from_date >= to_date:  # if premium order date > than end date
            user.premium_active = False
            premium_order.is_active = False
            user.save()
            premium_order.save()

        return response
