from django.urls import path,include
from .views import register_user
from .views import user_login
from .views import home
from .views import api_users
from .views import user_logout
from .views import membership_form
from .views import userdetail

app_name='caruser'

urlpatterns = [
    path('register/',register_user, name='register'),
    path('login/',user_login, name='login'),
    path('logout/',user_logout, name='logout'),
    path('home/',home, name='userhome'),
    path('membership/',membership_form, name='membership'),
    path('userdetail/',userdetail,name='user_detail'),
    path('api/v1/users/',api_users, name='all_user_api_v1'),
]