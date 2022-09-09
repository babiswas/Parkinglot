from django.urls import path,include
from .views import edit_lot,add_ticket,edit_ticket,delete_ticket,lot_detail,all_lots

app_name='parkinglot'

urlpatterns = [
    path('update_lot/<int:lotid>',edit_lot, name='edit_lot'),
    path('add_ticket/',add_ticket, name='create_ticket'),
    path('edit_ticket/<int:ticketid>',edit_ticket, name='edit_ticket'),
    path('delete_ticket/<int:ticketid>',delete_ticket, name='delete_ticket'),
    path('delete_ticket/<int:ticketid>',delete_ticket, name='delete_ticket'),
    path('lot/<int:lotid>',lot_detail, name='lot_detail'),
    path('lots/',all_lots, name='all_lots'),
]