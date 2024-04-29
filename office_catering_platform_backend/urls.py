"""office_catering_platform_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.authtoken.views import obtain_auth_token

from users.api.views import UserCreateAPIView, LoggedInUserInfoView, get_ip_info

schema_view = get_schema_view(
    openapi.Info(
        title="Live Streaming API",
        default_version='v1',
        description="Office Catering Platform Api description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="dpnrawthapa@mail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/api-auth/', include('rest_framework.urls')),
                  path("api/auth-token/", obtain_auth_token),
                  path('api/users/create/', UserCreateAPIView.as_view(), name='create_user'),
                  path('api/users/me/', LoggedInUserInfoView.as_view(), name='me'),
                  path('api/get_ip_info/', get_ip_info, name='get_ip_info'),
                  path("api/", include("office_catering_platform_backend.api_router")),
                  re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0),
                          name='schema-json'),
                  re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
                  re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
