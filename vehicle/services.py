import json

from .models import Vehicle, Location

def get_location():
    vehicle, created = Vehicle.objects.get_or_create(
        name='TestVehicle')
    location, created = Location.objects.get_or_create(vehicle=vehicle)
    return location


def update_locations(location_data):
    """
    reads a text file and updates with the locations
    """
    location_data = json.loads(location_data)
    
    with open("testdata.txt") as test_file:
        test_data = test_file.read()
    
    if test_data:
        test_data = json.loads(test_data)
        count = max(test_data[0].keys())
        test_data[0][int(count) + 1] = location_data
    else:
        test_data = [{1: location_data}, {'location_sequnce': 1}]

    with open("testdata.txt", "w") as test_file:
        json.dump(test_data, test_file)


def validate_data(post_data):
    try:
        json_locations = json.loads(post_data)
        return True
    except:
        return False
