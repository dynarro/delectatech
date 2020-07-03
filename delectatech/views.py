from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Restaurant, Segment
from .forms import RestaurantForm, SegmentForm


class RestaurantCreateView(CreateView):
    model = Restaurant
    template_name = 'delectatech/restaurant_new.html'
    form_class = RestaurantForm
    queryset = Restaurant.objects.all()
    success_url =  reverse_lazy('delectatech:restaurants_list')

    def form_valid(self, form):
        return super().form_valid(form)


class SegmentCreateView(CreateView):
    model = Segment
    template_name = 'delectatech/segment_new.html'
    form_class = SegmentForm
    queryset = Segment.objects.all()
    success_url =  reverse_lazy('delectatech:segments_list')

    def form_valid(self, form):
        return super().form_valid(form)


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
    success_url = reverse_lazy('delectatech:restaurant_detail')


class SegmentUpdateView(UpdateView):
    model = Segment
    fields = ["name", "average_popularity_rate", "average_satisfaction_rate",
              "average_price", "total_reviews", "restaurants"
             ]
    success_url = reverse_lazy('delectatech:segment_detail')


class RestaurantDeleteView(DeleteView):
    model = Restaurant
    success_url = reverse_lazy('delectatech:home')


class SegmentDeleteView(DeleteView):
    model = Segment
    success_url = reverse_lazy('delectatech:home')

def home(request):
    return render(request, 'delectatech/index.html', {})

def restaurants_list(request):
    restaurants = Restaurant.objects.all().order_by('city_name')
    return render(request, 'delectatech/restaurants_list.html', {'restaurants': restaurants})

def segments_list(request):
    segments = Segment.objects.all().order_by('name')
    return render(request, 'delectatech/segments_list.html',
    {'segments': segments})
"""
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
"""
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
