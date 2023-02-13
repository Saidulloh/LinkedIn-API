from rest_framework.routers import DefaultRouter

from apps.premium.views import PremiumApiViewSet, PremiumOrderApiViewSet


router = DefaultRouter()
router.register(
    prefix="list",
    viewset=PremiumApiViewSet
)

router.register(
    prefix="buy",
    viewset=PremiumOrderApiViewSet
)

urlpatterns = router.urls
