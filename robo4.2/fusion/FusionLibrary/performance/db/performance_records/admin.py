from django.contrib import admin
from .models import PerformanceRecord, FusionResource, FirmwareVersion


class PerformanceRecordAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['time', 'resource_id']}),
        ('Data', {'fields': ['duration', 'fw_version_id', 'is_asynchronous', 'within_threshold']}),
    ]

# Register your models here.
admin.site.register(PerformanceRecord, PerformanceRecordAdmin)
admin.site.register(FirmwareVersion)
admin.site.register(FusionResource)
