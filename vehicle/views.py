from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework import status
from rest_framework.response import Response

from vehicle.models import Location
from vehicle.services import get_location, update_locations, validate_data
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


class PopulateTestData(APIView):
    """
    This end point is used to acquire live test data to store in text file as json
    data can be used later to test on Android
    post data ex:
    {"locations": '{"lat": 1, "long": 1}''}
    """

    def post(self, request, format=None):
        new_location = request.data.get('locations')
        if validate_data(new_location):
            update_locations(new_location)
            return HttpResponse(status=201)
        return HttpResponse(status=400)
