from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_events, name='events'),
    path('<int:event_id>/', views.event_profile, name='event_profile'),
    path('map_view/', views.map_view, name='map_view'),
    path('add/', views.add_event, name='add_event'),
    path('event_instance/<int:eventinstance_id>/', views.event_instance_profile, name='event_instance_profile'),
    path('add_event_instance/', views.add_event_instance, name='add_event_instance'),
    path('edit/<int:event_id>/', views.edit_event, name='edit_event'),
    path('edit_event_instance/<int:eventinstance_id>/', views.edit_event_instance, name='edit_event_instance'),
    path('delete/<int:event_id>/', views.delete_event, name='delete_event'),
    path('event_link_options/', views.event_link_options, name='event_link_options'),
    path('event_connect/<int:event_id>/', views.event_connect, name='event_connect'),
    path('check_latlong/', views.check_latlong, name='check_latlong'),
    
]