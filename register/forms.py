from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from phonenumber_field.formfields import PhoneNumberField
from .models import Coordinator

class RegisterUserForm(UserCreationForm):
    phone = PhoneNumberField()
    club = forms.CharField(max_length=50,required=True)
    username = forms.CharField(max_length=50,required=True)
    first_name = forms.CharField(max_length=50,required=True)
    last_name = forms.CharField(max_length=50,required=True)
    email = forms.EmailField(max_length=50,required=True)
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self):
        user = super().save()
        club_name = self.cleaned_data.get('club')
        phone = self.cleaned_data.get('phone')
        coordinator = Coordinator(user=user, club=club_name, phone=phone)
        coordinator.save()
        return coordinator
        
    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['club'].widget.attrs['class'] = 'form-control'
        self.fields['phone'].widget.attrs['class'] = 'form-control'
        