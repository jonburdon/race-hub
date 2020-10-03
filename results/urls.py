from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_results, name='results'),
    path('<int:result_id>/', views.single_result, name='single_result'),
    path('result_lists/', views.all_result_lists, name='all_result_lists'),
    path('event/<eventinstance_id>', views.single_event_result_list, name='single_event_result_list'),
    path('add/', views.add_result, name='add_result'),    

]