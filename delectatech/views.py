from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from .models import Restaurant, Segment
from .forms import RestaurantForm, SegmentForm


class RestaurantDetailView(DetailView):
    model = Restaurant


class SegmentDetailView(DetailView):
    model = Segment


class RestaurantUpdateView(UpdateView):
    model = Restaurant
    fields = ["name", "street_address", "latitude", "longitude",
              "city_name", "popularity_rate", "satisfaction_rate",
              "total_reviews", "average_price"
             ]
    success_url = "/"


class SegmentUpdateView(UpdateView):
    model = Segment
    fields = ["name", "average_popularity_rate", "average_satisfaction_rate",
              "average_price", "total_reviews", "restaurants"
             ]
    success_url = "/"

def home(request):
    return render(request, 'delectatech/index.html', {})

def restaurants_list(request):
    restaurants = Restaurant.objects.all().order_by('city_name')
    return render(request, 'delectatech/restaurants_list.html', {'restaurants': restaurants})

def segments_list(request):
    segments = Segment.objects.all().order_by('name')
    return render(request, 'delectatech/segments_list.html',
    {'segments': segments})

def restaurant_new(request):
    if request.method == "POST":
        form = RestaurantForm(request.POST)
        if form.is_valid():
            restaurant = form.save(commit=False)
            restaurant.save()
            return redirect('restaurant_detail')
    else:
        form = RestaurantForm()
    return render(request, 'delectatech/restaurant_new.html', {'form': form})

def segment_new(request):
    if request.method == "POST":
        form = SegmentForm(request.POST)
        if form.is_valid():
            segment = form.save(commit=False)
            segment.save()
            return redirect('segments_list')
    else:
        form = SegmentForm()
    return render(request, 'delectatech/segment_new.html', {'form': form})
