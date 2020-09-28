from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_results, name='results'),
    path('<result_id>', views.single_result, name='single_result'),    

]