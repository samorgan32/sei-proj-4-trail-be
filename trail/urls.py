from django.urls import path
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from .views import WalkthroughViewSet, SlideViewSet

router = DefaultRouter()

router.register(r'walkthroughs', WalkthroughViewSet, basename='walkthrough')
router.register(r'slides', SlideViewSet, basename='slide')

urlpatterns = router.urls