from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView
from django.shortcuts import redirect, get_object_or_404
from django.utils import timezone
from django.conf import settings
from .models import URL, UrlVisit
from .serializers import URLSerializer


class URLRedirectAPIView(APIView):
    def get(self, request, uuid):
        url_instance = URL.objects.filter(uuid=uuid).first()

        if not url_instance:
            return Response({"error": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

        if url_instance.is_expired:
            return Response({"error": "Expired"}, status=status.HTTP_410_GONE)

        url_instance.clicks += 1

        # Add url visit
        today = timezone.now().date()
        ip_address = request.META.get("REMOTE_ADDR")
        daily_click, created = UrlVisit.objects.get_or_create(
            url=url_instance, 
            date=today, 
            ip_address=ip_address
        )
        daily_click.count += 1
        daily_click.save(update_fields=["count"])

        if url_instance.one_time_use:
            url_instance.delete()
        else:
            url_instance.save(update_fields=['clicks'])

        return redirect(url_instance.original_url)


class URLViewSet(viewsets.ModelViewSet):
    queryset = URL.objects.all()
    serializer_class = URLSerializer

    def list(self, request, *args, **kwargs):
        return Response(
            {"detail": "Listing URLs is not allowed."}, 
            status=status.HTTP_403_FORBIDDEN
        )

    def update(self, request, *args, **kwargs):
        return Response(
            {"detail": "Updating URLs is not allowed."}, 
            status=status.HTTP_403_FORBIDDEN
        )

    def partial_update(self, request, *args, **kwargs):
        return Response(
            {"detail": "Partial update is not allowed."}, 
            status=status.HTTP_403_FORBIDDEN
        )

    def destroy(self, request, *args, **kwargs):
        return Response(
            {"detail": "Deleting URLs is not allowed."}, 
            status=status.HTTP_403_FORBIDDEN
        )
