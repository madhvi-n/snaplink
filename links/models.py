from django.db import models
from django.conf import settings
from shortuuid.django_fields import ShortUUIDField
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import User


class URL(models.Model):
    uuid = ShortUUIDField(length=10, max_length=10, unique=True)
    original_url = models.URLField(max_length=2048, unique=True, db_index=True)
    new_url = models.CharField(
        max_length=100, unique=True, db_index=True, null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    expires_at = models.DateTimeField(default=timezone.now() + timedelta(days=7))
    clicks = models.PositiveIntegerField(default=0)
    one_time_use = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ["created_at"]
        verbose_name_plural = "URLs"

    def save(self, *args, **kwargs):
        if not self.new_url:
            self.new_url = f"{settings.BASE_URL}/{self.uuid}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.new_url}"

    @property
    def is_expired(self):
        return self.expires_at <= timezone.now() or (
            self.one_time_use and self.clicks > 0
        )


class UrlVisit(models.Model):
    url = models.ForeignKey(URL, on_delete=models.CASCADE, related_name="visits")
    date = models.DateField(default=timezone.now)
    count = models.PositiveIntegerField(default=0)
    ip_address = models.GenericIPAddressField()

    class Meta:
        unique_together = ("url", "date", "ip_address")
