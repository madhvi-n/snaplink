from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.throttling import ScopedRateThrottle
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import redirect, get_object_or_404
from django.utils import timezone
from django.conf import settings
from django.core.cache import cache
from .models import URL, UrlVisit
from .serializers import URLSerializer, URLReadOnlySerializer
from .mixins import MultiSerializerViewSetMixin


class URLRedirectAPIView(APIView):
    def get(self, request, uuid):
        cache_key = f"url_{uuid}"
        cached_url = cache.get(cache_key)
        if cached_url:
            return redirect(cached_url)

        url_instance = URL.objects.filter(uuid=uuid).first()

        if not url_instance:
            return Response({"error": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

        if url_instance.is_expired:
            return Response({"error": "Expired"}, status=status.HTTP_410_GONE)

        cache.set(cache_key, url_instance.original_url, timeout=settings.CACHE_TIMEOUT)

        url_instance.clicks += 1

        # Add url visit
        today = timezone.now().date()
        ip_address = request.META.get("REMOTE_ADDR")
        daily_click, created = UrlVisit.objects.get_or_create(
            url=url_instance, date=today, ip_address=ip_address
        )
        daily_click.count += 1
        daily_click.save(update_fields=["count"])

        if url_instance.one_time_use:
            url_instance.delete()
        else:
            url_instance.save(update_fields=["clicks"])

        return redirect(url_instance.original_url)


class URLCreateView(generics.CreateAPIView):
    queryset = URL.objects.all()
    serializer_class = URLSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = "create_url"


class URLDeleteView(generics.DestroyAPIView):
    """Allowing authenticated users to delete their urls"""

    queryset = URL.objects.all()
    throttle_classes = [ScopedRateThrottle]
    permission_classes = [IsAuthenticated]
    throttle_scope = "delete_url"

    def destroy(self, request, *args, **kwargs):
        if self.request.user and self.request.user.is_authenticated:
            url = self.get_object()
            if hasattr(url, user) and self.user == url.user:
                url.delete()
                return Response(
                    {"detail": "Deleted url successfully"}, status=status.HTTP_200_OK
                )
        return Response(
            {"detail": "Deleting URLs is not allowed."},
            status=status.HTTP_403_FORBIDDEN,
        )
