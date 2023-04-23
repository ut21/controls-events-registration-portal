import csv
from django.http import HttpResponse
from .models import Event
from .forms import EventForm
from django.shortcuts import render
import pandas as pd
from .resources import EventResource, EventReqsResource, CoordinatorResource, EventJudgesheetsResource, EventTravelsResource, EventLocationResource
# Create your views here.




def show_events(request):
    return render (request, 'events_portal/index.html', {
        #'clubs': Club.objects.all(),
        'events': Event.objects.all(),
        'events_user': events_user
    })

events_user = []

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        print("POST request detected")
        if form.is_valid():
            print(form.cleaned_data)
            author = request.user.coordinator
            new_event = form.save(author)
            events_user.append(new_event)
            print(events_user)
        return render(request, 'events_portal/after_adding_event.html', {'new_event': new_event})
    else:
        form = EventForm()
    return render(request, 'events_portal/user.html', {'form': form})


# def add_coordinator(request):
#     return render (request, 'events_portal/coord.html',{
#       "form": CoordForm(),
#     })

def event_csv(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename=events.csv'
	
	events=Event.objects.all()
	
	# Create a csv writer
	writer = csv.writer(response)
	# Designate The Model
	events = Event.objects.all()

	# Add column headings to the csv file
	writer.writerow(['name', 'desciption', 'date', 'time', 'location_pref_1', 'location_pref_2', 'location_pref_3', 'mics', 'projector', 'speakers', 'is_event_happening_for_the_first_time', 'judgesheet', 'registration_details', 'PrizeMoney', 'KindPoints'])

	# Loop Thu and output
	for event in events:
		writer.writerow([event.name, event.description, event.date, event.time, event.location_pref1, event.location_pref2, event.location_pref3, event.mics, event.projector, event.speakers, event.is_event_happening_for_the_first_time, event.judgesheet, event.registration_details, event.PrizeMoney, event.KindPoints])
	return response

def events_excel(request):
	event_resource = EventResource()
	dataset = event_resource.export()
	response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
	response['Content-Disposition'] = 'attachment; filename="events.xls"'
	return response
	
def events_reqs_excel(request):
    event_resource = EventReqsResource()
    dataset = event_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="events_reqs.xls"'
    return response

def coordinator_excel(request):
    coordinator_resource = CoordinatorResource()
    dataset = coordinator_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="coordinator.xls"'
    return response

def events_judgesheets_excel(request):
    event_resource = EventJudgesheetsResource()
    dataset = event_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="events_judgesheets.xls"'
    return response

def events_travels_excel(request):
    event_resource = EventTravelsResource()
    dataset = event_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="events_travels.xls"'
    return response

def events_location_excel(request):
    event_resource = EventLocationResource()
    dataset = event_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="events_location.xls"'
    return response