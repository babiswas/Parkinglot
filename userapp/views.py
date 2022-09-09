from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.contrib import auth
from django.contrib import messages

# Create your views here.


def register_user(request):

    '''Function based views to register user'''

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
                if form.save():
                    return redirect('userapp:login', permanent=True)
                else:
                    messages.error(request, 'Uable to save the form:')
                    return render(request, 'userapp/register.html', {'form': form, 'message': messages})
        else:
                messages.error(request, 'Form is invalid')
                return render(request, 'userapp/register.html', {'form': form, 'message': messages})
    form = RegisterForm()
    return render(request, 'userapp/register.html', {'form': form})

def user_login(request):

    '''Function based views for user login'''

    if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('carapp:carlist', permanent=True)
    return render(request, 'userapp/login.html')

def user_logout(request):

    '''Function based views for user logout'''

    auth.logout(request)
    return redirect('userapp:login', permanent=True)
