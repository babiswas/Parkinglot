from django.contrib import admin
from .models import Lot

# Register your models here.


class LotAdmin(admin.ModelAdmin):
    pass

admin.site.register(Lot,LotAdmin)
