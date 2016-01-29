from __future__ import unicode_literals

from django.db import models

# Create your models here.


class TimeStampModel(models.Model):

    created_ts = models.DateTimeField('created', auto_now_add=True)
    updated_ts = models.DateTimeField('updated', auto_now=True)
    is_active = models.BooleanField(default=True, db_index=True)

    class Meta:
        abstract = True


class Vehicle(TimeStampModel):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Location(TimeStampModel):

    vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
