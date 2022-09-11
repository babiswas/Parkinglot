from django.urls import path,include
from .views import add_car,get_all_cars,car_detail,edit_car,success,error,car_app_home

app_name='carapp'

urlpatterns = [
    path('add_car/',add_car, name='add_car'),
    path('cars/',get_all_cars, name='all_car'),
    path('car/<int:carid>',car_detail, name='car_detail'),
    path('success/',success, name='success'),
    path('error/',error, name='error'),
    path('edit/<int:carid>',edit_car, name='edit_car'),
    path('',car_app_home, name='car_home'),
]




