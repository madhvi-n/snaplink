from django.urls import path
from .views import URLCreateView, URLDeleteView

urlpatterns = [
    path("urls/", URLCreateView.as_view(), name="url-create"),
    path("urls/<int:pk>/", URLDeleteView.as_view(), name="url-delete"),
]
