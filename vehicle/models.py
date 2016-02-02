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
    """
    Basic Vehicle may be Bus, Car
    """
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Location(TimeStampModel):
    """
    A vehicle is tracked using this model. The track of the vehicle is stored in this model.
    Each instance of location is created when vehicle moving from point A to B(5 seconds)
    Need to refactor this model if required. To be stored as json to reduce database complexity
    """

    vehicle = models.ForeignKey('Vehicle', null=True, blank=True, on_delete=models.CASCADE)
    prev_lat = models.FloatField(null=True, blank=True)
    prev_long = models.FloatField(null=True, blank=True)
    current_lat = models.FloatField(null=True, blank=True)
    current_long = models.FloatField(null=True, blank=True)
