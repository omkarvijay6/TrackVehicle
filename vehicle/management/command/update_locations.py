import json

from django.core.management.base import BaseCommand

from vehicle.services import get_location

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

    location_sequence = test_data[1]["location_sequence"]

    if int(max(test_data[0].keys())) < location_sequence:
        test_data[1]["location_sequence"] = 1
    else:
        test_data[1]["location_sequence"] = location_sequence + 1
    
    geo_data = test_data[0][str(location_sequence)]
    update_location_obj(geo_data)
    with open("testdata.txt", "w") as test_file:
        json.dump(test_data, test_file)


class Command(BaseCommand):

    def handle(self, *args, **options):
        update_test_data()
