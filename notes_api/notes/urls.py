from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import NoteViewSet, RegisterView

router = DefaultRouter()

router.register(
    'notes',
    NoteViewSet,
    basename='notes'
)

urlpatterns = router.urls + [
    path('register/', RegisterView.as_view(), name='register'),
]