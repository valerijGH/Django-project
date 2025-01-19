from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api.views import ProfessionViewSet
from api.views import GeneralStatisticsViewSet
from api.views import DemandStatisticsViewSet, GeographyStatisticsViewSet, SkillViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="Документация для API проекта",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="your_email@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("api/token/", TokenObtainPairView.as_view(), name="get_token"),
    # path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    # path("api-auth/", include("rest_framework.urls")),
    path('api/', include('api.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("api/professions/", ProfessionViewSet.as_view({"get": "list"}), name="professions"),
    path("api/general-statistics/", GeneralStatisticsViewSet.as_view({"get": "list"}), name="general-statistics"),
    path("api/demand-statistics/", DemandStatisticsViewSet.as_view({"get": "list"}), name="demand_statistics"),
    path("api/geography-statistics/", GeographyStatisticsViewSet.as_view({"get": "list"}), name="geography_statistics"),
    path("api/skill/", SkillViewSet.as_view({"get": "list"}), name="skill"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
