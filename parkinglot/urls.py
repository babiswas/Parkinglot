from django.urls import path,include
from .views import add_ticket,inactivate_ticket,lot_detail,all_lots,success,error

app_name='parkinglot'

urlpatterns = [
    path('add_ticket/<int:lotid>',add_ticket, name='create_ticket'),
    path('edit_ticket/<int:ticketid>',inactivate_ticket, name='edit_ticket'),
    path('lot/<int:lotid>',lot_detail, name='lot_detail'),
    path('lots/',all_lots, name='all_lots'),
    path('success/',success, name='success'),
    path('error/',error, name='error'),
]