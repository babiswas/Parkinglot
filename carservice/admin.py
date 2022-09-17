from django.contrib import admin
from .models import CarService
# Register your models here.




# Register your models here.


class CarServiceAdmin(admin.ModelAdmin):
    pass

admin.site.register(CarService,CarServiceAdmin)
