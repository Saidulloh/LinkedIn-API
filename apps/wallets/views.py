from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from django.contrib.auth import get_user_model

from apps.wallets.models import Wallet
from apps.wallets.serializers import WalletSerializer


User = get_user_model()


class WalletApiViewSet(GenericViewSet,
                       CreateModelMixin,
                       ListModelMixin):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def create(self, request, *args, **kwargs):
        user = User.objects.get(pk=request.user.id)
        user.wallet += int(request.data['amount'])
        user.save()
        return super().create(request, *args, **kwargs)
