from django import forms

from .models import Restaurant, Segment


class RestaurantForm(forms.ModelForm):

    class Meta:
        model = Restaurant
        fields = ('name', 'street_address', 'latitude', 'longitude',
        'city_name', 'popularity_rate', 'satisfaction_rate', 'total_reviews',
        'average_price')


class SegmentForm(forms.ModelForm):

    class Meta:
        model = Segment
        fields = ('name', 'average_popularity_rate',
        'average_satisfaction_rate', 'average_price','total_reviews',
        'restaurants')
