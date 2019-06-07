from rest_framework import serializers
from performance_records.models import PerformanceRecord, FusionResource, FirmwareVersion


class PerformanceRecordSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PerformanceRecord
        fields = ('id', 'time', 'resource_id', 'duration', 'fw_version_id', 'is_asynchronous', 'within_threshold')


class FusionResourceSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = FusionResource
        fields = ('id', 'resource', 'action', 'condition', 'asynchronous_time', 'test_case')


class FirmwareVersionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = FirmwareVersion
        fields = ('id', 'fusion_release', 'feature_set', 'platform', 'delta')
