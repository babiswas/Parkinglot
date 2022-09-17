from django.contrib import admin
from .models import CarGroup

# Register your models here.


class CarGroupAdmin(admin.ModelAdmin):
    pass

admin.site.register(CarGroup,CarGroupAdmin)
