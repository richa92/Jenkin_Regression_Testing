from django.db import models


# Create your models here.
class FusionResource(models.Model):
    id = models.AutoField(primary_key=True)
    resource = models.CharField(max_length=100)
    action = models.CharField(max_length=50)
    condition = models.CharField(max_length=100)
    asynchronous_time = models.IntegerField()
    test_case = models.CharField(max_length=200, blank=True, default='')

    class Meta:
        unique_together = (("resource", "action", "condition", "test_case"),)

    def __str__(self):              # __unicode__ on Python 2
        string = "[%s] %s %s" % (str(self.id), self.action, self.resource)
        if self.condition != 'None':
            string += " (%s)" % self.condition
        return string


class FirmwareVersion(models.Model):
    id = models.AutoField(primary_key=True)
    fusion_release = models.CharField(max_length=100)
    feature_set = models.CharField(max_length=100)
    platform = models.CharField(max_length=100, default='C7000')
    delta = models.CharField(max_length=200, blank=True, default='')

    def __str__(self):
        string = "[%s] %s %s (%s)" % (str(self.id), self.platform, self.fusion_release, self.feature_set)
        if self.delta != '':
            string += " + " + self.delta
        return string


class PerformanceRecord(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.DateTimeField(max_length=100)
    resource_id = models.ForeignKey(FusionResource)
    duration = models.IntegerField()
    fw_version_id = models.ForeignKey(FirmwareVersion)
    is_asynchronous = models.BooleanField(default=False)
    within_threshold = models.BooleanField(default=False)

    def __str__(self):
        string = "[%s]: Resource %s - %s Firmware - %sms" % (str(self.id), str(self.resource_id), str(self.fw_version_id), str(self.duration))
        return string

    class Meta:
        ordering = ('id',)
