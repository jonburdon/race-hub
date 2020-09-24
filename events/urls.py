from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_events, name='events'),
    path('<event_id>', views.event_profile, name='event_profile'),
    path('map_view/', views.map_view, name='map_view'),
]