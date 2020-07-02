import json
from django.core.management.base import BaseCommand
from delectatech.models import Restaurant, Segment

class Command(BaseCommand):
    # imports json file on the db
    def handle(self, *args, **kwargs):
        with open('/home/doraly/Documents/Prueba Tecnica/restaurants_input.json') as data_file:
            json_data = json.load(data_file)

            for restaurant_data in json_data:
                restaurant = Restaurant(**restaurant_data)
                restaurant.save()
            self.stdout.write("restaurants imported")

        with open('/home/doraly/Documents/Prueba Tecnica/segments_input.json') as segments_file:
            seg_data = json.load(segments_file)

            for segment_data in seg_data:
                for data in seg_data[3]:
                    segment = Segment(data)
                    segment.save()
            self.stdout.write("segments imported")
