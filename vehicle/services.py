import json

from .models import Vehicle, Location

def get_location():
    vehicle, created = Vehicle.objects.get_or_create(
        name='TestVehicle')
    location, created = Location.objects.get_or_create(vehicle=vehicle)
    return location

def update_locations(test_data, new_locations):
    new_locations = json.loads(new_locations)
    if test_data.locations:
        testdata_locations = json.loads(test_data.locations)
        count = max(testdata_locations.keys())
        testdata_locations[int(count) + 1] = new_locations
    else:
        testdata_locations = {1: new_locations}
    test_data.locations = json.dumps(testdata_locations)
    test_data.save()
