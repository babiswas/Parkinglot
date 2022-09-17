from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .forms import RegisterForm,MemberForm
from django.contrib import auth
from django.contrib import messages
from .serializer import UserSerializer
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import renderer_classes,api_view
from django.db import transaction
from django.http import HttpResponse


# Create your views here.


def register_user(request):

    '''Function based views to register user'''

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
                user=form.save()
                if user:
                    group=Group.objects.get(name='GUEST')
                    user.groups.add(group)
                    user.save()
                    return redirect('caruser:login', permanent=True)
                else:
                    #messages.error(request, 'Uable to save the form:')
                    return render(request, 'caruser/register.html', {'form': form, 'message': messages})
        else:
                #messages.error(request, 'Form is invalid')
                return render(request, 'caruser/register.html', {'form': form, 'message': messages})
    form = RegisterForm()
    return render(request, 'caruser/register.html', {'form': form})


def home(request):

    '''Home page for carusers'''

    return render(request,'caruser/home.html')

def user_login(request):

    '''Function based views for user login'''

    if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('caruser:userhome', permanent=True)
            else:
                return HttpResponse('<h1>Error</h1>')
    return render(request, 'caruser/login.html')

def user_logout(request):

    '''Function based views for user logout'''

    auth.logout(request)
    return redirect('caruser:login', permanent=True)

@api_view(('GET',))
@renderer_classes((JSONRenderer,))
def api_users(request):

    '''App users list using api view and json renderer'''

    all_user=User.objects.all()
    users=UserSerializer(all_user,many=True)
    return Response(users.data)


def membership_form(request):

    '''Membership form for joining a group...'''


    groups = Group.objects.all()
    if request.method == "POST":
            with transaction.atomic():
                group = request.POST.get('name')
                mygroup = Group.objects.get(name=group)
                user = User.objects.get(id=request.user.id)
                user.groups.clear()
                user.groups.add(mygroup)
                return redirect('caruser:user_detail')
            return render(request, 'caruser/error.html')
    form = MemberForm()
    return render(request,'caruser/member.html',{'form':form})


def userdetail(request):

    '''Membership form for joining a group...'''

    user = User.objects.get(id=request.user.id)
    groups = user.groups.all()
    return render(request,'caruser/member_detail.html',{'groups':groups,'user':user})






