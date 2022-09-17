from django.shortcuts import render
from django.shortcuts import redirect
from .models import Car
from django.contrib.auth.models import User
from .forms import CarForm,CarUpdateForm
from django.http import HttpResponse
from .serializer import CarSerializer
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from caruser.serializer import UserSerializer
from rest_framework.decorators import renderer_classes,api_view
from django.db import transaction
from .models import CarGroup

# Create your views here.


def get_all_cars(request):

    '''Get all the cars of the user'''

    cars=Car.objects.filter(carowner_id=request.user.id)
    return render(request,'carapp/cars.html',{'cars':cars})


def get_all_cars_parked(request):

    '''Get all the parked cars of the user'''

    cars=Car.parkedcar.filter(carowner_id=request.user.id).all()
    return render(request,'carapp/cars.html',{'cars':cars})


def get_all_cars_unparked(request):

    '''Get all the unparked cars of the user'''

    cars=Car.unparkedcar.filter(carowner_id=request.user.id).all()
    return render(request,'carapp/cars.html',{'cars':cars})

def car_detail(request,carid):

    '''Method to get the details of the car'''

    car=Car.objects.get(pk=carid)
    return render(request,'carapp/car_detail.html',{'car':car})

def add_car(request):

        '''Method to add a new car'''

        if request.method == "POST":
            with transaction.atomic():
                form=CarForm(request.POST)
                car=Car()
                car.carowner=request.user
                car.carname=request.POST.get('carname')
                car.carcolor=request.POST.get('carcolor')
                car.carnumber = request.POST.get('carnumber')
                car.cargroup=CarGroup.objects.get(name=request.groups.all()[0].name)
                car.save()
                return redirect('carapp:car_detail',carid=car.id)
            return HttpResponse('<h1>Error</h1>')

        form = CarForm()
        return render(request, 'carapp/add_car.html', {'form': form})


def edit_car(request,carid):

    '''Method to add a new car'''

    car=Car.objects.get(pk=carid)
    if request.method == "POST":
        car.carname = request.POST.get('carname')
        car.carcolor = request.POST.get('carcolor')
        car.save()
        return redirect('carapp:car_detail',carid=car.id)

    form = CarUpdateForm(instance=car)
    return render(request, 'carapp/update_car.html', {'form': form})



def success(request):

    '''Service for success mesage:'''

    return HttpResponse('<h1>Success</h1>')

def error(request):

    '''Service for error message:'''

    return HttpResponse('<h1>Error</h1>')

def car_app_home(request):

    '''Car app home service'''

    return render(request,'carapp/carapp_home.html')


@api_view(('GET',))
@renderer_classes((JSONRenderer,))
def api_user_cars(request):

    '''App users list using api view and json renderer'''

    all_cars_user=Car.objects.filter(carowner_id=request.user.id)
    cars=CarSerializer(all_cars_user,many=True)
    return Response(cars.data)






