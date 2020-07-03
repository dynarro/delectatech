from django.urls import path
from . import views


urlpatterns = [
     path('', views.home, name='home'),
     # Restaurant urls
     path('restaurant/new/', views.RestaurantCreateView.as_view(), name='restaurant_new'),
     path('restaurant/list/', views.restaurants_list, name='restaurants_list'),
     path('restaurant/<pk>/', views.RestaurantDetailView.as_view(), name="restaurant_detail"),
     path('restaurant/<pk>/update/', views.RestaurantUpdateView.as_view(), name="restaurant_update"),
     path('restaurant/<pk>/delete/', views.RestaurantDeleteView.as_view(), name="restaurant_delete"),
     # Segment urls
     path('segment/new/', views.SegmentCreateView.as_view(), name='segment_new'),
     path('segment/list/', views.segments_list, name='segments_list'),
     path('segment/<pk>/', views.SegmentDetailView.as_view(), name="segment_detail"),
     path('restaurant/<pk>/update/', views.SegmentUpdateView.as_view(), name="segment_update"),
     path('restaurant/<pk>/delete/', views.SegmentDeleteView.as_view(), name="segment_delete"),
]

app_name = 'posts'
