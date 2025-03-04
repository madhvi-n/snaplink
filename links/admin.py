from django.contrib import admin
from .models import URL, UrlVisit


# Register your models here.
@admin.register(URL)
class URLAdminAdmin(admin.ModelAdmin):
    list_display = ("id", "original_url", "new_url", "is_expired", "one_time_use", "clicks")



@admin.register(UrlVisit)
class UrlVisitAdmin(admin.ModelAdmin):
    list_display = ("id", "url", "count", "ip_address")