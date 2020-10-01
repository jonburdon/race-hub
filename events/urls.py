from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_events, name='events'),
    path('<int:event_id>/', views.event_profile, name='event_profile'),
    path('map_view/', views.map_view, name='map_view'),
    path('add/', views.add_event, name='add_event'),
    path('edit/<int:event_id>/', views.edit_event, name='edit_event'),
]