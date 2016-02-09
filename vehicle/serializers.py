import json
from geopy.distance import vincenty

from rest_framework import serializers

from vehicle.models import Location

class LocationSerializer(serializers.ModelSerializer):
    velocity = serializers.SerializerMethodField()

    class Meta:
        model = Location
        fields = ('prev_lat', 'prev_long', 'current_lat', 'current_long', 'velocity',)

    
    def get_velocity(self, location_obj):
        prev_location = (location_obj.prev_lat, location_obj.prev_long)
        current_location = (location_obj.current_lat, location_obj.current_long)
        distance = vincenty(prev_location, current_location).meters
        time = 5
        velocity = distance/5.0
        velocity_in_km = velocity*(18/5.0)
        return velocity_in_km
