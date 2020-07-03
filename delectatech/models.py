import uuid
from django.db import models
from django.conf import settings
from django.utils import timezone


class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    street_address = models.CharField(max_length=400, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    city_name = models.CharField(max_length=100)
    popularity_rate = models.FloatField(null=True)
    satisfaction_rate = models.FloatField(null=True)
    total_reviews = models.BigIntegerField(null=True)
    uidentifier = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    average_price = models.FloatField(null=True)

    def __str__(self):
        return  self.name

class Segment(models.Model):
    name = models.CharField(max_length=200)
    uidentifier = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    average_popularity_rate = models.FloatField(null=True)
    average_satisfaction_rate = models.FloatField(null=True)
    average_price = models.FloatField(null=True)
    total_reviews = models.BigIntegerField(null=True)
    restaurants = models.ManyToManyField(Restaurant)

    def __str__(self):
        return  self.name
