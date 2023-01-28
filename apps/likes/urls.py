from rest_framework.routers import DefaultRouter

from apps.likes.views import PostLikeApiViewSet, CommentLikeApiViewSet


router = DefaultRouter()
router.register(
    prefix="post_like",
    viewset=PostLikeApiViewSet
)

router.register(
    prefix="comment_like",
    viewset=CommentLikeApiViewSet
)

urlpatterns = router.urls
