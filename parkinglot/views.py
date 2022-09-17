from django.shortcuts import render
from django.shortcuts import redirect
from .models import Lot,Ticket
from carapp.models import Car
from django.contrib.auth.models import User
from .forms import TicketForm,LotForm,InactivateForm
from django.http import HttpResponse
from django.db import transaction
from .serializer import LotSerializer,TicketSerializer
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from rest_framework import serializers
from carapp.serializer import CarSerializer
from rest_framework.decorators import renderer_classes,api_view



def lot_detail(request,lotid):

        '''Get the details of the lot and all the tickets created for this lot'''

        with transaction.atomic():
            parking_lot = Lot.objects.get(pk=lotid)
            tickets = Ticket.objects.filter(ticketowner_id=request.user.id).filter(lot_id=parking_lot.id)
            return render(request, 'parkinglot/lot_detail.html', {'parkinglot': parking_lot,'tickets':tickets})
        return HttpResponse('<h1>Error<h1>')


def all_lots(request):

    '''Get the list of lots'''
    all_lots = Lot.objects.all()
    return render(request, 'parkinglot/all_lots.html', {'all_lots': all_lots })

def available_lots(request):

    '''Get all available lots...'''
    lots=Lot.available_lot.all()
    return render(request, 'parkinglot/all_lots.html', {'all_lots': lots})

def occupied_lots(request):

    '''Get all available lots...'''
    lots=Lot.occupied_lot.all()
    return render(request, 'parkinglot/all_lots.html', {'all_lots': lots})


def all_tickets(request,lotid):

    tickets=Ticket.objects.filter(ticketowner_id=request.user.id).filter(lot_id=lotid)
    return render(request, 'parkinglot/lot_tickets.html', {'tickets': tickets})

def all_tickets_user(request):

    '''Get all the tickets created by the user'''

    tickets=Ticket.objects.filter(ticketowner_id=request.user.id)
    return render(request, 'parkinglot/tickets.html', {'tickets': tickets})

def ticket_car(request):

    '''A service to show the car and ticket info...'''

    ticket_car=Ticket.objects.select_related('vehicle').filter(ticketowner_id=request.user.id)
    return render(request, 'parkinglot/ticket_car.html', {'ticket_car': ticket_car})




def add_ticket(request,lotid):

    '''Method to create a lot ticket'''

    lot = Lot.objects.get(pk=lotid)
    cars= Car.objects.filter(carowner_id=request.user.id)
    if lot.state=="AVAILABLE":
            print("Entered the available block:")
            if request.method == "POST":
                with transaction.atomic():
                    lot.state='OCCUPIED'
                    lot.save()
                    ticket=Ticket()
                    ticket.lot=lot
                    ticket.ticketowner=request.user
                    ticket.vehicle=Car.objects.get(pk=request.POST.get('vehicle'))
                    ticket.save()
                    return redirect('parkinglot:lot_detail',permanent=True,lotid=lotid)
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
            return redirect('parkinglot:lot_detail',permanent=True,lotid=lot.id)
        return redirect('parkinglot:error', permanent=True)
    form = InactivateForm(instance=ticket)
    return render(request, 'parkinglot/inactivate_ticket.html', {'form': form})


def success(request):
    return HttpResponse('<h1>Success</h1>')

def error(request):
    return HttpResponse('<h1>Error</h1>')



def parking_home(request):

    '''Parking app home service'''

    return render(request,'parkinglot/parking_home.html')

@api_view(('GET',))
@renderer_classes((JSONRenderer,))
def api_lots(request):

    '''List of parking lots using api.'''

    all_lots=Lot.objects.all()
    lots=LotSerializer(all_lots,many=True)
    return Response(lots.data)


@api_view(('GET',))
@renderer_classes((JSONRenderer,))
def api_tickets(request):

    '''List of tickets using api.'''

    all_tickets=Ticket.objects.filter(ticketowner_id=request.user.id)
    lot_tickets=TicketSerializer(all_tickets,many=True)
    return Response(lot_tickets.data)

@api_view(('GET',))
@renderer_classes((JSONRenderer,))
def mytickets(request):

    '''List of tickets using api.'''
    with transaction.atomic():
        try:
            user=User.objects.get(id=request.user.id)
            mytickets=user.ticket_set.all()
            all_my_tickets=TicketSerializer(mytickets,many=True)
            return Response(all_my_tickets.data,status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(('GET',))
@renderer_classes((JSONRenderer,))
def mycars(request):

    '''List of tickets using api.'''
    with transaction.atomic():
        try:
            user=User.objects.get(id=request.user.id)
            mycars=user.car_set.all()
            all_my_cars=CarSerializer(mycars,many=True)
            return Response(all_my_cars.data,status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


