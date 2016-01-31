from .models import Vehicle, Location

def get_location():
    vehicle, created = Vehicle.objects.get_or_create(name='TestVehicle')
    location = Location.objects.first()
    return location
