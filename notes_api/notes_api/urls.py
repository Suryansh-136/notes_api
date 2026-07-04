from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import ( TokenObtainPairView,TokenRefreshView,)
from django.views.generic import TemplateView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Notes API",
      default_version='v1',
      description="API for managing notes",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    #admin site
    path('admin/',admin.site.urls),

    #api notes
    path('api/', include('notes.urls')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),


    #api HTML page
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('auth-page/',TemplateView.as_view(template_name='auth.html'),name='auth-page'),


    #swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
