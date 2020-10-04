from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_results, name='results'),
    path('<int:result_id>/', views.single_result, name='single_result'),
    path('<int:result_id>/', views.result_detail, name='result_detail'),
    path('result_lists/', views.all_result_lists, name='all_result_lists'),
    path('event/<eventinstance_id>', views.single_event_result_list, name='single_event_result_list'),
    path('add/', views.add_result, name='add_result'),
    path('edit_full_result/<int:result_id>/', views.edit_full_result, name='edit_full_result'),
    path('submit_virtual_result/<int:result_id>/', views.edit_result_time_only, name='edit_result_time_only'),        

]