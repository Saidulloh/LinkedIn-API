from rest_framework.routers import DefaultRouter

from apps.wallets.views import WalletApiViewSet


router = DefaultRouter()
router.register(
    prefix="",
    viewset=WalletApiViewSet
)

urlpatterns = router.urls
