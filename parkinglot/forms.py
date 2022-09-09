from django.forms import ModelForm
from .models import Lot
from .models import Ticket


class LotForm(ModelForm):

    '''LotForm for creating and updating a Lot'''

    class Meta:
        model=Lot
        fields=['floor','slot','name','state']

class TicketForm(ModelForm):

    '''TicketForm for updating tickets'''

    class Meta:
        model= Ticket
        fields = ['vehicle']

class InactivateForm(ModelForm):

    '''InactivateForm for making the ticket Inactive'''

    class Meta:
        model= Ticket
        fields = ['ticketstate']
