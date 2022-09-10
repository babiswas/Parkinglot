from django.shortcuts import render
from django.shortcuts import redirect
from .models import Lot,Ticket
from carapp.models import Car
from django.contrib.auth.models import User
from .forms import TicketForm,LotForm,InactivateForm
from django.http import HttpResponse
from django.db import transaction


def lot_detail(request,lotid):

    '''Get the details of the lot'''

    parking_lot = Lot.objects.get(pk=lotid)
    return render(request, 'parkinglot/lot_detail.html', {'parkinglot': parking_lot })

def all_lots(request):

    '''Get the list of lots'''

    all_lots = Lot.objects.all()
    return render(request, 'parkinglot/all_lots.html', {'all_lots': all_lots })


def add_ticket(request,lotid):

    '''Method to create a lot ticket'''

    lot = Lot.objects.get(pk=lotid)
    cars= Car.objects.filter(carowner_id=request.user.id)
    if lot.state=="AVAILABLE":
            if request.method == "POST":
                with transaction.atomic():
                    lot.state='OCCUPIED'
                    lot.save()
                    ticket=Ticket()
                    ticket.lot=lot
                    ticket.ticketowner=request.user
                    ticket.vehicle=Car.objects.get(pk=request.POST.get('vehicle'))
                    ticket.save()
                    return redirect('parkinglot:success',permanent=True)
            return redirect('parkinglot:error',permanent=True)
            form = TicketForm()
            form.fields['vehicle'].queryset=cars
            return render(request, 'parkinglot/lot_ticket.html', {'form': form })
    else:
        return HttpResponse('<h1>Lot Occupied</h1>')


def inactivate_ticket(request,ticketid):

    '''Update the tickets using this service.'''

    ticket=Ticket.objects.get(pk=ticketid)
    if request.method == "POST":
        with transaction.atomic():
            lotid=ticket.lot.id
            lot=Lot.objects.get(pk=lotid)
            lot.state='AVAILABLE'
            lot.save()
            ticket.ticketstate='INACTIVE'
            ticket.save()
            return redirect('parkinglot:success', permanent=True)
        return redirect('parkinglot:error', permanent=True)
    form = InactivateForm(instance=ticket)
    return render(request, 'parkinglot/inactivate_ticket.html', {'form': form})


def success(request):
    return HttpResponse('<h1>Success</h1>')

def error(request):
    return HttpResponse('<h1>Error</h1>')
