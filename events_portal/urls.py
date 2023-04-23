from django.urls import path
from . import views

urlpatterns = [
    #path('show_events/', views.index, name='index'),
    path('', views.add_event, name='add_event'),
    path('show_events/', views.show_events, name='show_events'),
    path('events_csv/', views.event_csv, name='event_csv'),
    path('events_excel/', views.events_excel, name='event_excel'),
    path('events_reqs_excel/', views.events_reqs_excel, name='event_reqs_excel'),
    path('coordinator_excel/', views.coordinator_excel, name='coordinator_excel'),
    path('events_judgesheets_excel/', views.events_judgesheets_excel, name='events_judgesheets_excel'),
    path('events_travels_excel/', views.events_travels_excel, name='events_travels_excel'),
    path('events_location_excel/', views.events_location_excel, name='events_location_excel'),
]