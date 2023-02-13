from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="LinkedIn API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.IsAuthenticated,),
)

api_urlpatterns = [
    path('chats/', include('apps.chats.urls')),
    path('comments/', include('apps.comments.urls')),
    path('contact_details/', include('apps.contact_details.urls')),
    path('contacts/', include('apps.contacts.urls')),
    path('favorites/', include('apps.favorites.urls')),
    path('likes/', include('apps.likes.urls')),
    path('messages/', include('apps.message.urls')),
    path('posts/', include('apps.posts.urls')),
    path('premium/', include('apps.premium.urls')),
    path('users/', include('apps.users.urls')),
    path('wallets/', include('apps.wallets.urls')),

    # authorization
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),

    # swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    # api
    path('', include(api_urlpatterns))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)