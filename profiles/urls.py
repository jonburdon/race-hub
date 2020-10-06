from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='my_racehub'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('add_racehub_friend/', views.add_racehub_friend, name='add_racehub_friend'),
]