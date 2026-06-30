from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import ( TokenObtainPairView,TokenRefreshView,)
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/',admin.site.urls),

    #api notes
    path('api/', include('notes.urls')),

     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

     path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    #api djoser
    # path('auth/', include('djoser.urls')),       # Register: /auth/users/
    # path('auth/', include('djoser.urls.jwt')),   # Login: /auth/jwt/create/

    #api HTML page
    path('auth-page/',TemplateView.as_view(template_name='auth.html'),name='auth-page'),

]
