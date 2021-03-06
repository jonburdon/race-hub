from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_results, name='results'),
    path('<int:result_id>/', views.single_result, name='single_result'),
    # path('<int:result_id>/', views.result_detail, name='result_detail'),
    path('result_lists/', views.all_result_lists, name='all_result_lists'),
    path('event/<int:eventinstance_id>/', views.single_event_result_list, name='single_event_result_list'),
    path('review_virtual_results/<int:eventinstance_id>/', views.review_virtual_results, name='review_virtual_results'),
    path('add/<int:eventinstance_id>/', views.add_result, name='add_result'),
    path('edit_full_result/<int:result_id>/', views.edit_full_result, name='edit_full_result'),
    path('submit_virtual_result/<int:result_id>/', views.edit_result_time_only, name='edit_result_time_only'),
    path('transfer_result/<int:result_id>/', views.transfer_result, name='transfer_result'),
    path('download_results/', views.download_results, name='download_results'),
    path('verify_result/<int:result_id>/', views.verify_result, name='verify_result'),
    path('unverify_result/<int:result_id>/', views.unverify_result, name='unverify_result'),
    path('delete/<int:result_id>/', views.delete_result, name='delete_result'),           

]