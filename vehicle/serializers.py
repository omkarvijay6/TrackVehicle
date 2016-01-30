from rest_framework import serializers
from vehicle.models import Location

class VehicleLocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = ('prev_lat', 'prev_long', 'current_lat', 'current_long',)


    def to_representation(self, location_obj):
        ret = {}
        ret['previous_latitude'] = location_obj.prev_lat
        ret['previous_longitude'] = location_obj.prev_long
        ret['current_latitude'] = location_obj.current_lat
        ret['current_longitude'] = location_obj.current_long
        return ret
