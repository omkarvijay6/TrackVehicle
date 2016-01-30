from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView

from vehicle.models import Location
from vehicle.services import get_location
from vehicle.serializers import VehicleLocationSerializer
# Create your views here.

class VehicleLocation(RetrieveUpdateAPIView):
    serializer_class = VehicleLocationSerializer

    def get_object(self):
        location = get_location()
        return location
