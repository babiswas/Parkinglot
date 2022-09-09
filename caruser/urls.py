from django.urls import path,include
from .views import register_user
from .views import user_login
from .views import home

app_name='caruser'

urlpatterns = [
    path('register/',register_user, name='register'),
    path('login/',user_login, name='login'),
    path('home/',home, name='userhome'),
]