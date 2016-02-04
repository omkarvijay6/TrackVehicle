from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView, UpdateAPIView
from rest_framework import status
from rest_framework.response import Response

from vehicle.models import Location, TestData
from vehicle.services import get_location, update_locations
from vehicle.serializers import LocationSerializer, TestDataSerializer
# Create your views here.

class VehicleLocation(RetrieveUpdateAPIView):
    """
    Endpoint updates the location of the vehicle in post request
    Returns the location of the vehicle in get request
    payload:
    {
        "prev_lat": 123.2,
        "prev_long": 12353.3,
        "current_lat": 1252.5,
        "current_long": 1945.3,

    }
    prev lat and long used to calculate the distance travelled and velocity of the vehicle
    """
    serializer_class = LocationSerializer

    def get_object(self):
        location = get_location()
        return location


class PopulateTestData(UpdateAPIView):
    """
    This end point is used to acquire live test data to store in Location model
    without vehicle.
    data can be used later to test on Android
    """
    serializer_class = TestDataSerializer

    def get_object(self):
        test_data, created = TestData.objects.get_or_create(name='RealTimeMobileGPS')
        return test_data

    def perform_update(self, serializer):
        test_data = self.get_object()
        new_locations = self.request.data.get('locations')
        update_locations(test_data, new_locations)
