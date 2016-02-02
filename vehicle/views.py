from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView

from vehicle.models import Location
from vehicle.services import get_location
from vehicle.serializers import LocationSerializer
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


class GetTestData(ListCreateAPIView):
    """
    This end point is used to acquire live test data to store in Location model
    without vehicle.
    data can be used later to test on Android
    """
    serializer_class = LocationSerializer
    queryset = Location.objects.all()

