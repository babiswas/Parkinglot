from django.shortcuts import render
from django.shortcuts import redirect
from .models import Lot,Ticket
from django.contrib.auth.models import User
from .forms import TicketForm,LotForm


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



def add_ticket(request):
    pass


def edit_ticket(request):
    pass


def delete_ticket(request):
    pass
