from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.forms import ModelForm




class RegisterForm(UserCreationForm):

    '''Form to register user'''

    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    username = forms.CharField(max_length=100, required=True)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def save(self, commit=True):

        '''Method to save the user'''

        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            return user




class MemberForm(forms.Form):
    '''Form for selecting member group...'''

    DEMO_CHOICES=(("GUEST","GUEST"),("PREMIUM","PREMIUM"),("SILVER","SILVER"),("STANDARD", "STANDARD"))
    name = forms.MultipleChoiceField(choices=DEMO_CHOICES)



