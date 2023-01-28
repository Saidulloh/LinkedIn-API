from rest_framework.routers import DefaultRouter

from apps.posts.views import PostApiViewSet, PostDetailApiViewSet


router = DefaultRouter()
router.register(
    prefix='',
    viewset=PostApiViewSet
)

router.register(
    prefix="post",
    viewset=PostDetailApiViewSet
)

urlpatterns = router.urls
