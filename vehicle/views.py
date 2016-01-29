from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from location.models import Location
# Create your views here.


class VehicleLocation(ListAPIView):
	queryset = Location.objects.all()