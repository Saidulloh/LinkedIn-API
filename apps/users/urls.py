from rest_framework.routers import DefaultRouter

from apps.users.views import UserApiViewSet, UserCreateApiViewSet, EducationApiViewSet, WorkExperienceApiViewSet


router = DefaultRouter()
router.register(
    prefix="user",
    viewset=UserApiViewSet
)

router.register(
    prefix="",
    viewset=UserCreateApiViewSet
)

router.register(
    prefix="education",
    viewset=EducationApiViewSet
)

router.register(
    prefix="work_experience",
    viewset=WorkExperienceApiViewSet
)

urlpatterns = router.urls
