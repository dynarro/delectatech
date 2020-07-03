import json
from django.core.management.base import BaseCommand
from delectatech.models import Restaurant, Segment

class Command(BaseCommand):
    # imports json file on the db
    def handle(self, *args, **kwargs):
        with open('/home/doraly/Documents/Prueba Tecnica/restaurants_input.json') as data_file:
            json_data = json.load(data_file)

            # Imports only 10 objects to avoid to much data
            for restaurant_data in json_data[:10]:
                restaurant = Restaurant(**restaurant_data)
                restaurant.save()
            self.stdout.write("restaurants imported successfully!")

        with open('/home/doraly/Documents/Prueba Tecnica/segments_input.json') as segments_file:
            seg_data = json.load(segments_file)

            for data in seg_data:
                # Imports only 10 objects to avoid to much data
                for restaurant in data['restaurants'][:10]:
                    segment = Segment(restaurant)
                    segment.save()
            self.stdout.write("segments imported successfully!")
