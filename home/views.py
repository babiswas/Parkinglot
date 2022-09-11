from django.shortcuts import render

# Create your views here.

def home(request):

    '''Home page for the user'''

    return render(request,'base.html')
