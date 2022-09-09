from django.shortcuts import render
from django.shortcuts import redirect
from .models import Lot,Ticket
from django.contrib.auth.models import User
from .forms import TicketForm,LotForm,InactivateForm
from django.http import HttpResponse


def edit_lot(request,lotid):

    '''Method to update the lot'''

    instance=Lot.objects.get(pk=lotid)
    if request.method == "POST":
        form = LotForm(request.POST,instance=instance)
        if form.is_valid():
                if form.save():
                    return redirect('caruser:login', permanent=True)
                else:
                    return render(request, 'parkinglot/edit_lot.html', {'form': form, 'message': messages})
        else:
                return render(request, 'parkinglot/edit_lot.html', {'form': form, 'message': messages})
    form = LotForm(instance=instance)
    return render(request, 'parkinglot/edit_lot.html', {'form': form})


def lot_detail(request,lotid):

    '''Get the details of the lot'''

    parking_lot = Lot.objects.get(pk=lotid)
    return render(request, 'parkinglot/lot_detail.html', {'parkinglot': parking_lot })

def all_lots(request):

    '''Get the list of lots'''

    all_lots = Lot.objects.all()
    return render(request, 'parkinglot/all_lots.html', {'all_lots': all_lots })



def add_ticket(request,lotid):

    '''Method to create a ticket'''

    lot = Lot.objects.get(pk=lotid)
    cars= Car.objects.filter(carowner_id=request.user.id)
    if lot.state=="AVAILABLE":
        if request.method == "POST":
            form = LotForm(request.POST)
            if form.is_valid():
                if form.save():
                    return redirect('caruser:login', permanent=True)
                else:
                    return render(request, 'parkinglot/edit_lot.html', {'form': form, 'message': messages})
            else:
                return render(request, 'parkinglot/edit_lot.html', {'form': form, 'message': messages})
    form = TicketForm()
    form.fields[]
    return render(request, 'parkinglot/lot_ticket.html', {'form': form ,'cars':cars})


def add_ticket(request,lotid):

    '''Method to create a lot ticket'''

    lot = Lot.objects.get(pk=lotid)
    cars= Car.objects.filter(carowner_id=request.user.id)
    if lot.state=="AVAILABLE":
            if request.method == "POST":
                ticket=Ticket()
                ticket.lot=lot
                ticket.ticketowner=request.user
                ticket.vehicle=request.POST.get('vehicle')
                ticket.save()
                return redirect('parkinglot:success',permanent=True)
            form = TicketForm()
            form.fields['vehicle'].queryset=cars
            return render(request, 'parkinglot/lot_ticket.html', {'form': form })


def inactivate_ticket(request,ticketid):

    '''Update the tickets using this service.'''

    ticket=Ticket.objects.get(pk=ticketid)
    if lot.state == "AVAILABLE":
        if request.method == "POST":
            ticket = Ticket()
            ticket.lot = lot
            ticket.ticketowner = request.user
            ticket.vehicle = request.POST.get('vehicle')
            ticket.save()
            return redirect('parkinglot:success', permanent=True)
        form = InactivateForm()
        form.fields['vehicle'].queryset = cars
        return render(request, 'parkinglot/lot_ticket.html', {'form': form})


def delete_ticket(request):
    pass


def sucess(request):
    return HttpResponse('<h1>Success</h1>')

def error(request):
    return HttpResponse('<h1>Error</h1>')
