from django.shortcuts import render
from django.shortcuts import redirect
from .models import Car
from django.contrib.auth.models import User
from .forms import CarForm,CarUpdateForm
from django.http import HttpResponse

# Create your views here.


def get_all_cars(request):

    '''Get all the cars of the user'''

    cars=Car.objects.filter(carowner_id=request.user.id)
    return render(request,'carapp/cars.html',{'cars':cars})

def car_detail(request,carid):

    '''Method to get the details of the car'''

    car=Car.objects.get(pk=carid)
    return render(request,'carapp/car_detail.html',{'car':car})

def add_car(request):

        '''Method to add a new car'''

        if request.method == "POST":
            form=CarForm(request.POST)
            car=Car()
            car.carowner=request.user
            car.carname=request.POST.get('carname')
            car.carcolor=request.POST.get('carcolor')
            car.carnumber = request.POST.get('carnumber')
            car.save()
            return redirect('carapp:car_detail',carid=car.id)

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



