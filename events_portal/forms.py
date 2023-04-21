from django.forms import ModelForm
from .models import Event
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EventForm(ModelForm):
    class Meta:
        model = Event
        # fields = '__all__'
        fields = ['name', 'description', 'date', 'time', 'location_pref1', 'location_pref2', 'location_pref3', 'mics', 'projector', 'speakers', 'is_event_happening_for_the_first_time', 'judgesheet', 'registration_details', 'PrizeMoney', 'KindPoints']

    def save(self, author):
        event = super(EventForm, self).save(commit=False)
        event.author = author
        event.save()
        return event
        
# class NewUserForm(UserCreationForm):
# 	email = forms.EmailField(required=True)

# 	class Meta:
# 		model = Coordinator
# 		fields = "__all__"

# 	def save(self, commit=True):
# 		user = super(NewUserForm, self).save(commit=False)
# 		user.email = self.cleaned_data['email']
# 		if commit:
# 			user.save()
# 		return user
