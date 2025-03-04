from django.urls import path, include
from rest_framework.routers import DefaultRouter
from links.views import URLViewSet


router = DefaultRouter()
router.register(r'urls', URLViewSet, basename="urls")

urlpatterns = [
    path('', include(router.urls)),
]
