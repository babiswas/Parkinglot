from django.forms import ModelForm
from .models import Car


class CarForm(ModelForm):

    '''Carform to populate the car model'''

    class Meta:
        model=Car
        fields=['carname','carnumber','carcolor']

class CarUpdateForm(ModelForm):

    '''Carform to populate the car model'''

    class Meta:
        model=Car
        fields=['carname','carcolor','cargroup']

