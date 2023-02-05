from rest_framework.routers import DefaultRouter

from apps.contact_details.views import ContactAppendApiViewSet


router = DefaultRouter()
router.register(
    prefix="",
    viewset=ContactAppendApiViewSet
)

urlpatterns = router.urls
