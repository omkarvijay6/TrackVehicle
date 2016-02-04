import json

from rest_framework import serializers
from vehicle.models import Location, TestData

class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = ('prev_lat', 'prev_long', 'current_lat', 'current_long',)


class TestDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestData
        fields = ('locations', 'location_sequence_id',)


    def validate_locations(self, locations):
        try:
            json_locations = json.loads(locations)
        except:
            raise serializers.ValidationError('locations is not JSON Serializable')
        return locations
