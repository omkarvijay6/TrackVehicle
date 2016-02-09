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
        count = max(map(int, test_data[0].keys()))
        test_data[0][int(count) + 1] = location_data
    else:
        test_data = [{1: location_data}, {'location_sequence': 1}]

    with open("testdata.txt", "w") as test_file:
        json.dump(test_data, test_file)


def validate_data(post_data):
    try:
        json_locations = json.loads(post_data)
        return True
    except:
        return False


def update_location_obj(geo_data):
    """
    update the current and previous location
    """
    location_obj = get_location()
    data_dict = {'prev_lat': location_obj.current_lat, 'prev_long': location_obj.current_long,
                 'current_lat': geo_data['lat'], 'current_long': geo_data['long']}
    for k, v in data_dict.iteritems():
        setattr(location_obj, k, v)
    location_obj.save()


def update_test_data():
    """
    populate the location object and update the testdata json to have a track of current position
    through location_sequence
    """
    with open("testdata.txt") as test_file:
        test_data = json.loads(test_file.read())

    if max(map(int, test_data[0].keys())) == test_data[1]["location_sequence"]:
        test_data[1]["location_sequence"] = 1
    else:
        test_data[1]["location_sequence"] = test_data[1]["location_sequence"] + 1
    location_sequence = test_data[1]["location_sequence"]
    geo_data = test_data[0][str(location_sequence)]
    update_location_obj(geo_data)
    with open("testdata.txt", "w") as test_file:
        json.dump(test_data, test_file)
