from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='my_racehub'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('add_racehub_friend/', views.add_racehub_friend, name='add_racehub_friend'),
    path('add_family_and_friends/', views.add_nonracehubfriend, name='add_nonracehubfriend'),
    path('add_athlete_profile/', views.add_athlete_profile, name='add_athlete_profile'),
]