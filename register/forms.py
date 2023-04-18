from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 
from register.models import Club
from django.forms import ModelForm

class RegisterUserForm(UserCreationForm):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
	first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
	last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
	club = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
	

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


	def __init__(self, *args, **kwargs):
		super(RegisterUserForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['class'] = 'form-control'
		
class ClubForm(ModelForm):
    class Meta:
        model = Club
        fields = "__all__"
    # club = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    # coordinator = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    # coordinator_number = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class':'form-control'}))
    

    # def __init__(self, *args, **kwargs):
    #     super(ClubForm, self).__init__(*args, **kwargs)

    #     self.fields['Club'].widget.attrs['class'] = 'form-control'
    #     self.fields['coordinator_number'].widget.attrs['class'] = 'form-control'