from django.contrib import admin
from .models import PerformanceRecord, FusionResource, FirmwareVersion


class PerformanceRecordAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['resource']}),
        ('Data', {'fields': ['action', 'duration', 'fw_version_id', 'synchronous', 'within_threshold']}),
    ]

# Register your models here.
admin.site.register(PerformanceRecord, PerformanceRecordAdmin)
admin.site.register(FirmwareVersion)
admin.site.register(FusionResource)
