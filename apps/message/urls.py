from rest_framework.routers import DefaultRouter

from apps.message.views import MessageApiViewSet, MessageListDetailApiViewSet


router = DefaultRouter()
router.register(
    prefix="create",
    viewset=MessageApiViewSet
)

router.register(
    prefix="",
    viewset=MessageListDetailApiViewSet
)

urlpatterns = router.urls
