from django.urls import path,include
from .views import register_user
from .views import user_login
from .views import home
from .views import user_logout

app_name='caruser'

urlpatterns = [
    path('register/',register_user, name='register'),
    path('login/',user_login, name='login'),
    path('logout/',user_logout, name='logout'),
    path('home/',home, name='userhome'),
]