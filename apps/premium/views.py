from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, DestroyModelMixin
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.decorators import action
from django.contrib.auth import get_user_model

from apps.premium.models import Premium, PremiumOrder
from apps.premium.serializers import PremiumSerialzer, PremiumOrderSerializer
from utils.permissions import IsOwner


User = get_user_model()


class PremiumApiViewSet(GenericViewSet,
                        ListModelMixin,
                        RetrieveModelMixin):
    queryset = Premium.objects.all()
    serializer_class = PremiumSerialzer
    permission_classes = [IsAuthenticated]

    @action(
        detail=False, permission_classes=[IsOwner], methods=["get"]
    )
    def active_premium(self, request):
        queryset = PremiumOrder.objects.get(is_active=True, owner=request.user)
        serializer = PremiumOrderSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PremiumOrderApiViewSet(GenericViewSet,
                             CreateModelMixin,
                             DestroyModelMixin,
                             ListModelMixin):
    queryset = PremiumOrder.objects.all()
    serializer_class = PremiumOrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def create(self, request, *args, **kwargs):
        premium = Premium.objects.get(id=int(request.data['premium']))
        active_premium = PremiumOrder.objects.filter(owner=request.user, is_active=True)
        user = User.objects.get(pk=request.user.id)
        if active_premium:
            return Response({'Error': f'You alredy have active premium!'})
        elif user.wallet >= premium.price:
            user.wallet -= premium.price  # mines price to wallet
            user.premium_active = True  # change premium active to True
            user.save()  # saving
            return super().create(request, *args, **kwargs)
        else:
            return Response({'Error': 'You do not have pretty amount!'})

    def get_queryset(self):
        return PremiumOrder.objects.filter(owner=self.request.user)
