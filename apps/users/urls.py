from rest_framework.routers import DefaultRouter

from apps.users.views import UserApiViewSet, UserCreateApiViewSet


router = DefaultRouter()
router.register(
    prefix="user",
    viewset=UserApiViewSet
)

router.register(
    prefix="",
    viewset=UserCreateApiViewSet
)

urlpatterns = router.urls
