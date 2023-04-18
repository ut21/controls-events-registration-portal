from django.shortcuts import render
from .models import Event
from .forms import EventForm
# Create your views here.

# def index(request):
#     return render (request, 'events_portal/index.html', {
#         #'clubs': Club.objects.all(),
#         'events': Event.objects.all()
#     })
def add_event(request):
    return render (request, 'events_portal/user.html',{
      "form": EventForm(),
    })

# def add_coordinator(request):
#     return render (request, 'events_portal/coord.html',{
#       "form": CoordForm(),
#     })