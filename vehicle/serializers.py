from rest_framework import serializers
from vehicle.models import Location

class VehicleLocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = ('prev_lat', 'prev_long', 'current_lat', 'current_long',)


class TestDataSerializer(serializers.ModelSerializer):

	class Meta:
		model = Location
		fields = ('prev_lat', 'prev_long', 'current_lat', 'current_long',)
